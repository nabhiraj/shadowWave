#here i will start my audio experimentation
import simpleaudio as sa#this library file is useless
import sounddevice as sd#this is very usefull
fs = 44100  # Sample rate
seconds = 5  # Duration of recording
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()
print('done with recording')
print('now will play the recording')
print(myrecording)
sd.play(myrecording)
sd.wait()
#print('starting the thing')
#ba=bytearray([2,2,2,1,1,1,1,1]*10*44100)
#baa=bytes(ba)
#t=sa.play_buffer(ba,2,2,44100)
#t.wait_done()
#print('ending the thing')