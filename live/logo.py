def add_logo_to_video(video_path, new_video_path, vendor):
    import moviepy as mp
    from moviepy.video.fx import Margin
    from django.conf import settings
    import os
    import glob
    video = mp.VideoFileClip(video_path)
    logo = (mp.ImageClip(os.path.join(settings.BASE_DIR, "media/", vendor.vendor_profile.logo.path))
              .with_duration(video.duration)
              .resized(height=int(video.w/13)) # if you need to resize...
              .with_effects([Margin(margin_size=30,opacity=0)])
              .with_position(("left","bottom")))
    final = mp.CompositeVideoClip([video, logo])
    final.write_videofile(new_video_path)
    for f in glob.glob(str(settings.BASE_DIR) + '*TEMP_MPY_wvf_snd.mp3'):
        os.remove(f)
    return new_video_path
