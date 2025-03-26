import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lotteh.settings')
import django
django.setup()
from django.conf import settings
from live.models import VideoRecording, VideoCamera
from live.models import get_file_path
import traceback
for recording in VideoRecording.objects.filter(processed=True, uploaded=False).order_by('-last_frame'):
    camera = VideoCamera.objects.get(name=recording.camera, user=recording.user)
    if camera.upload:
        import os
        from django.conf import settings
        try:
            if not recording.file or not os.path.exists(recording.file.path):
                print('Getting file from bucket for upload')
                full_path = os.path.join(settings.BASE_DIR, 'media/', get_file_path(None, 'rec.mp4'))
                with recording.file_processed.storage.open(str(recording.file_processed.name), mode='rb') as bucket_file:
                    with open(full_path, "wb") as video_file:
                        video_file.write(bucket_file.read())
                    video_file.close()
                bucket_file.close()
                recording.file = full_path
                recording.save()
        except: print(traceback.format_exc())
        from recordings.youtube import upload_youtube
        try:
            from better_profanity import profanity
            upload_youtube(camera.user, recording.file.path, profanity.censor(camera.title[:67-len(recording.last_frame.strftime('%A %B %d, %Y %H:%M:%S'))]) + ' - ' + recording.last_frame.strftime('%A %B %d, %Y %H:%M:%S'), profanity.censor(camera.description) + ' - ' + profanity.censor(recording.transcript[:4000 - 3]), [tag for tag in camera.tags], category='22', privacy_status='public', age_restricted=not recording.public)
            recording.uploaded = True
        except:
            recording.uploaded = False
            print(traceback.format_exc())
        recording.save()
    break
