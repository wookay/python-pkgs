import sys
sys.path.append('..')
from lib.logging import print_info

import numpy
isapprox = numpy.allclose

import librosa

y, sr = librosa.load(librosa.util.example_audio_file(), duration=5)
print_info('y', y)
print_info('sr (samples)', sr)
print_info('type(y)', type(y))
print_info('isapprox y[-5:]', isapprox(y[-5:], [-0.057152, -0.05973774, -0.06121843, -0.05893796, -0.0626892]))

duration = librosa.get_duration(y=y, sr=sr)
print_info('duration (time)', duration)

tempo, beats = librosa.beat.beat_track(y, sr=sr)
print_info('tempo', tempo)
print_info('beats (frames)', beats)

beats_samples = librosa.frames_to_samples(beats)
print_info('beats (samples)', beats_samples)

beats_time = librosa.frames_to_time(beats)
print_info('beats (time)', beats_time)

hop_length = 512
onset_frames = librosa.onset.onset_detect(y, sr=sr, hop_length=hop_length, units='frames')
print_info('onset (frames)', onset_frames)

onset_samples = librosa.frames_to_samples(onset_frames)
print_info('onset (samples)', onset_samples)

# librosa.output.write_wav('example_audio_file_5s.wav', y, sr)
