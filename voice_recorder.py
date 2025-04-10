import sounddevice as sd
'''sounddevice is a Python library used to play and record audio.
It provides access to your computer’s microphone and speakers using the underlying PortAudio library
— but with a clean and Pythonic interface.
'''
from scipy.io.wavfile import write
'''importing the write function from the scipy.io.wavfile module 
— a part of the SciPy library — which allows you to save audio data as a .wav file.
'''
fs=44100 #This sets the sample rate for recording or playing audio.
'''
fs is short for "frequency sampling".
44100 means you're capturing 44,100 audio samples per second.
This is the standard sample rate used for CD-quality audio.
'''
seconds=int(input("Enter the time duration in seconds: "))

print("Recording...\n")

# Record audio
record_voice=sd.rec(int(seconds*fs),samplerate=fs,channels=2,dtype='int16')

'''
sd.rec(...)	Calls the rec() function from the sounddevice library to start recording
seconds * fs	Total number of samples to record (duration × sample rate)
samplerate=fs	Tells it to use the sample rate (e.g., 44100 samples/sec)
channels=2	Records in stereo (2 channels); use 1 for mono
record_voice = ...	Saves the recorded audio as a NumPy array in the variable record_voice
'''

sd.wait()# Wait until recording is finished

#save the recorded audio in a file
write("your_audio.wav",fs,record_voice)
'''
write:-A function from scipy.io.wavfile used to save .wav files
fs:-The sample rate (e.g., 44100 Hz) — needed so the file knows how fast to play back the audio
record_voice:-The actual audio data (stored as a NumPy array) that you recorded earlier
'''

print("Finished...\nPlease check 'your_audio.wav'.")