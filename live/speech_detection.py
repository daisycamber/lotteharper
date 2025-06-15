def detect_speech(input_mp4, vad_mode):
#    import moviepy as mp
    import uuid
    from django.conf import settings
    import os
#    clip = mp.VideoFileClip(input_mp4)
    output_wav = os.path.join(settings.BASE_DIR, "temp/data/{}.wav".format(str(uuid.uuid4())))
    os.system('ffmpeg -i {} -ac 1 -ar 8000 {}'.format(input_mp4, output_wav))
    from pydub import AudioSegment
    audio_file = AudioSegment.from_file(output_wav, format='wav')
#    normalized_audio = audio_file.normalize()
    output_wav2 = os.path.join(settings.BASE_DIR, "temp/data/{}.wav".format(str(uuid.uuid4())))
    quieter_audio = audio_file.normalize() - 40
    quieter_audio.export(output_wav2, format='wav')
    os.remove(output_wav)
#    clip.audio.write_audiofile(output_wav, codec='pcm_s16le')
    import webrtcvad
    import wave
    vad = webrtcvad.Vad(int(vad_mode))
#    vad.set_mode(3)
    with wave.open(output_wav2, "rb") as wf:
        sample_rate = wf.getframerate()
        audio_data = wf.readframes(wf.getnframes())
    frame_duration = 30
    frame_bytes = int(sample_rate * frame_duration / 1000) * 2
    output = False
    for i in range(0, len(audio_data), frame_bytes):
        frame = audio_data[i:i + frame_bytes]
        if len(frame) == frame_bytes:
            is_speech = vad.is_speech(frame, sample_rate)
            if is_speech: output = True
    os.remove(output_wav2)
    return output
