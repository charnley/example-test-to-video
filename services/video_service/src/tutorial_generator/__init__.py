import logging
from pathlib import Path

from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip
from tutorial_generator.video_funcs import generate_video
from tutorial_generator.speech_funcs import generate_audio

logger = logging.getLogger(__name__)

def synchronize_video_audio(video_filename, audio_filenames, timestamps, remove_first_section=False):

    video = VideoFileClip(str(video_filename))

    # if trim_start > 0:
    #     video = video.subclip(trim_start)

    trim_start = 0

    audio_clips = []

    for audio_path, timestamp in zip(audio_filenames, timestamps):

        audio = AudioFileClip(str(audio_path))
        adjusted_start = timestamp - trim_start

        if adjusted_start >= 0:
            audio_clips.append(audio.with_start(adjusted_start))

    # Composite audio and apply to video
    final_audio = CompositeAudioClip(audio_clips)
    final_video = video.with_audio(final_audio)

    # Generate output filename
    output_path = video_filename.parent / f"{video_filename.stem}_merged{video_filename.suffix}"
    final_video.write_videofile(str(output_path), audio_codec="aac")

    return output_path


def generate_tutorial(name, voice, actions, texts, remove_first_section=False):

    logger.info(f"Generating {name} tutorial")

    tmp_dir = Path("tmp_videos")
    video_name = f"{name}"

    assert len(actions) == len(texts)

    logger.info(f"Generating audio files")

    audio_filenames = []

    for i, text in enumerate(texts):

        filename = tmp_dir / f"section_{i}"
        filename = generate_audio(voice, text, filename)
        audio_filenames.append(filename)

        logger.info(f"Finished {filename}")

    logger.info(f"Generating video file")

    timestamps = generate_video(
        Path(video_name),
        actions,
    )

    video_filename = tmp_dir / Path(video_name).with_suffix(".webm")

    synchronize_video_audio(video_filename, audio_filenames, timestamps, remove_first_section=remove_first_section)

    return True
