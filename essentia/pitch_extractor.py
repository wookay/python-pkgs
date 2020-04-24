import sys
sys.path.append('..')
from lib.logging import print_info

from essentia import standard
import librosa

audio_file = librosa.util.example_audio_file()
loader = standard.MonoLoader(filename=audio_file)
audio = loader()

pitch_extractor = standard.PredominantPitchMelodia()
pitch_values, pitch_confidence = pitch_extractor(audio)

onsets, durations, notes = standard.PitchContourSegmentation()(pitch_values, audio)
print_info('onsets', onsets)
print_info('durations', durations)
print_info('notes', notes)
