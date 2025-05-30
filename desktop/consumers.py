import json, random, time, asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect, get_object_or_404
from users.models import Profile
from urllib.parse import parse_qs
import datetime, subprocess, threading

width = None
height = None
log = {}
pids = {}

@sync_to_async
def get_user(id):
    user = User.objects.get(id=int(id))
    if not (user.profile.admin or user.is_superuser): return False
    return True

@sync_to_async
def check_token(user_id, token):
    user = User.objects.get(id=int(user_id))
    import urllib.parse
    from security.crypto import decrypt
    return user.profile.check_shell_token(decrypt(urllib.parse.unquote(token)))

@sync_to_async
def get_auth(user_id, session_key):
    from security.models import UserSession
    sess = UserSession.objects.filter(user__id=user_id, session_key=session_key).order_by('-timestamp')
    for s in sess:
        if s.authorized: return True
    return False


# Send the setting to the server from foreign user
class DesktopConsumer(AsyncWebsocketConsumer):
    chat_user = None
    token = None
    connected = False
    pid = None
    async def connect(self):
        query_params = parse_qs(self.scope["query_string"].decode())
        auth = await get_user(self.scope['user'].id)
        import urllib.parse
        token = await check_token(self.scope['user'].id, query_params['token'][0])
        auth2 = await get_auth(self.scope['user'].id, self.scope['session'].session_key)
        print('Auth 1? {}'.format(str(auth)))
        print('Auth 2? {}'.format(str(auth2)))
        if not token:
            print('Token invalid for shell')
            return
        if not (auth and auth2): return
        await self.accept()
        self.connected = True
        user = await get_user(self.scope['user'].id)
        await self.send(text_data='connect')

    async def disconnect(self, close_code):
        self.connected = False
        pass

    # This function receive messages from WebSocket.
    async def receive(self, text_data):
        global background
        global background_key
        global background_mouse
        global background_pointer
        global pids
        command = text_data
        if not self.token:
            self.token = text_data
            self.background = AsyncEvent(self.token)
            self.background.start()
            self.background_key = AsyncEvent_key(self.token)
            self.background_key.start()
            self.background_mouse = AsyncEvent_mouse(self.token)
            self.background_mouse.start()
            self.background_pointer = AsyncEvent_pointer(self.token)
            self.background_pointer.start()
            self.pid = str(random.randint(11, 99))
            pids[self.token] = self.pid
            os.system("sudo Xvfb :{} -ac -screen 0 1024x768x24 &".format(str(self.pid)))
            os.system('xvfb-run --server-args=":{} -screen 0 1366x768x24" firefox &'.format(str(self.pid)))
            global width
            global height
            print(str(self.pid))
            await asyncio.sleep(5)
            width, height = [int(a) for a in str(subprocess.check_output("DISPLAY=:{}".format(str(self.pid)) + " xrandr | grep '*' | awk '{print $1}'", shell=True))[2:-3].split('x')]
            return
        if text_data:
            inp = text_data
            keys,mouse,pointer = inp.split('|')
            self.background_key.event_list.append(keys)
            self.background_mouse.event_list.append(mouse)
            self.background_pointer.event_list.append(pointer)
            randname = get_random_string(10)
            cmd = "DISPLAY=:{} {}python {}/image_generator.py {} {}".format(str(self.pid), str(os.path.join(settings.BASE_DIR, 'venv/bin/')), str(settings.BASE_DIR), str(self.pid), self.pid + '.png')
            print(cmd)
            os.system(cmd)
            f = open(os.path.join(settings.BASE_DIR, 'temp/', "{}.png".format(self.pid)), "rb")
            greeting = f.read()
#            os.remove(os.path.join(settings.BASE_DIR, 'temp/', "{}.png".format(randname)))
            await self.send(bytes_data=greeting)
        pass
    pass

def control_events(msg, token):
    global pids
    try:
        keys,mouse,pointer = msg.split('|')
        key_events = keys.split(',')
        for event in key_events:
            if event != "":
                res = os.popen("DISPLAY=:{} {}python {}/keypress.py ".format(pids[token], str(os.path.join(settings.BASE_DIR, 'venv/bin/')), str(settings.BASE_DIR)) + event).read()
        m_events = mouse.split(',')
        for event in m_events:
            if event != "":
                x,y,e=[int(float(a)) for a in event.split(' ')]
                x=str((x*width)/1000.0)
                y=str((y*height)/1000.0)
                e1=str(abs(e))
                if e > 0:
                    os.system("DISPLAY=:{} xdotool mousemove ".format(pids[token]) +x+" "+y+" mousedown "+e1)
                else:
                    os.system("DISPLAY=:{} xdotool mousemove ".format(pids[token]) +x+" "+y+" mouseup "+e1)
        x,y=[int(float(a)) for a in pointer.split(',')]
        x=str((x*width)/1000.0)
        y=str((y*height)/1000.0)
        os.system("DISPLAY=:{} xdotool mousemove ".format(pids[token]) +x+" "+y)
    except ValueError:
        pass


def key_control_events(msg, token):
    key_events = msg.split(',')
    global log
    global pids
    for event in key_events:
        if event != "":
            res = os.popen("DISPLAY=:{} {}python {}/keypress.py ".format(pids[token], str(os.path.join(settings.BASE_DIR, 'venv/bin/')), settings.BASE_DIR) + event).read()
            log[token] = res

def mouse_control_events(msg, token):
    m_events = msg.split(',')
    global pids
    global width
    global height
    for event in m_events:
        if event != "":
            x,y,e=[int(float(a)) for a in event.split(' ')]
            x=str((x*width)/1000.0)
            y=str((y*height)/1000.0)
            e1=str(abs(e))
            if e > 0:
                os.system("DISPLAY=:{} xdotool mousemove ".format(pids[token]) +x+" "+y+" mousedown "+e1)
            else:
                os.system("DISPLAY=:{} xdotool mousemove ".format(pids[token]) +x+" "+y+" mouseup "+e1)


def pointer_control_events(msg, token):
    x,y=[int(float(a)) for a in msg.split(',')]
    x=str((x*width)/1000.0)
    y=str((y*height)/1000.0)
    global pids
    os.system("DISPLAY=:{} xdotool mousemove ".format(pids[token]) +x+" "+y)

class AsyncEvent(threading.Thread):
    def __init__(self, token):
        threading.Thread.__init__(self)
        self.event_list = []
        self.token = token

    def run(self):
        while 1:
            if len(self.event_list) != 0:
                control_events(self.event_list.pop(0), self.token)


class AsyncEvent_key(threading.Thread):
    def __init__(self, token):
        threading.Thread.__init__(self)
        self.event_list = []
        self.token = token

    def run(self):
        while 1:
            if len(self.event_list) != 0:
                key_control_events(self.event_list.pop(0), self.token)

class AsyncEvent_mouse(threading.Thread):
    def __init__(self, token):
        threading.Thread.__init__(self)
        self.event_list = []
        self.token = token

    def run(self):
        while 1:
            if len(self.event_list) != 0:
                mouse_control_events(self.event_list.pop(0), self.token)

class AsyncEvent_pointer(threading.Thread):
    def __init__(self, token):
        threading.Thread.__init__(self)
        self.event_list = []
        self.token = token

    def run(self):
        while 1:
            if len(self.event_list) != 0:
                pointer_control_events(self.event_list.pop(0), self.token)

