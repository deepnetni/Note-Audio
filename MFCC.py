import numpy as np
import scipy
from scipy.io import wavfile
from scipy import signal
from matplotlib import pyplot as plt
from scipy.fftpack import dct
import pyaudio
import wave

def play(filename):
    CHUNK = 1024
    wf = wave.open(filename, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()
    p.terminate()

# the wave file can be downloaded under
# http://www.voiptroubleshooter.com/open_speech/american.html

# play("OSR_us_000_0010_8k.wav")

# get audio signals
rate, sig = wavfile.read("OSR_us_000_0010_8k.wav")

# get the first 3.5s signals
sig = sig[0:int(rate * 3.5)]

plt.subplot(411)
plt.plot(sig)
plt.grid()

# 1.预加重

b=np.array([1, -0.97])
sig_filter = signal.lfilter(b, a=1, x=sig)
plt.subplot(412)
plt.plot(sig_filter)
plt.grid()

# 2.分帧

frame_ms = 25
overlap_ms = 15
frame_stride_ms = frame_ms - overlap_ms

frame_length, frame_step = int(frame_ms * rate / 1000.0), int(frame_stride_ms * rate / 1000.0)
N = len(sig_filter)
frame_n_ = int(np.ceil((N - frame_length) / frame_step))

# 长度补零
pad_len = frame_n_ * frame_step + frame_length
pad_z = np.zeros(pad_len - N)
pad_signal = np.append(sig_filter, pad_z)

# one frame per line
indices = np.tile(np.arange(0, frame_length), (frame_n_, 1)) + np.array([x for x in np.arange(0, frame_n_ * frame_step, frame_step)]).reshape(-1, 1)
frames = pad_signal[np.mat(indices).astype(np.int32, copy=False)]

# 3. 加窗

# frames *= 0.54 - 0.46 * numpy.cos((2 * numpy.pi * n) / (frame_length - 1))
frames *= np.hamming(frame_length)

# 4. 傅立叶变换和功率谱

fft_len = 512
mag_frames = np.absolute(np.fft.rfft(frames, fft_len))
print("mag.shape: ", mag_frames.shape)
# power spectrum
power_frames = (mag_frames**2) * (1.0 / fft_len)

# plt.subplot(413)
# plt.plot(power_frames)

# 5. Mel 滤波器组

low_freq_mel = 0
high_freq_mel = 2592*np.log10(1 + (rate / 2) / 700)
mel_filter_n = 40
mel_points = np.linspace(low_freq_mel, high_freq_mel, mel_filter_n + 2)
# convert mel frequency to Hz units
hz_points = 700 * (10**(mel_points / 2592) - 1)

# n in the frame_length
bin_points = np.floor((fft_len + 1) * hz_points / rate)
fbank = np.zeros((mel_filter_n, int(np.floor(fft_len / 2 + 1))))

for i in range(1, mel_filter_n + 1):
    f_m_minus = int(bin_points[i - 1])
    f_m = int(bin_points[i])
    f_m_plus = int(bin_points[i + 1])
    for k in range(f_m_minus, f_m):
        fbank[i - 1, k] = (k - bin_points[i - 1]) / (bin_points[i] - bin_points[i - 1])
    for k in range(f_m, f_m_plus):
        fbank[i - 1, k] = (bin_points[i + 1] - k) / (bin_points[i + 1] - bin_points[i])

# power spectrum & fbank are both frequency-domain functions, time-domain filtering equals frequency-domain multiplication;
# np.dot 矩阵乘法
filter_banks = np.dot(power_frames, fbank.T)
print(power_frames.shape, fbank.shape)
# replace negative value to eps
filter_banks = np.where(filter_banks == 0, np.finfo(float).eps, filter_banks)
# dB
filter_banks = 20 * np.log10(filter_banks)

# keep the 2:13 cepstrum coefficients and drop the others.
num_ceps = 12
mfcc = dct(filter_banks, type=2, axis=1, norm="ortho")[:, 1:(num_ceps+1)]
(nframes, ncoeff) = mfcc.shape

n = np.arange(ncoeff)
cep_lifter =22
lift = 1 + (cep_lifter / 2) * np.sin(np.pi * n / cep_lifter)
mfcc *= lift

mfcc -= (np.mean(mfcc, axis=0) + 1e-8)
print("mfcc.shape: ", mfcc.shape)

# plt.figure()
# plt.imshow(np.flipud(mfcc.T), cmap=plt.cm.jet, aspect=0.2, extent=[0,mfcc.shape[0],0,mfcc.shape[1]])#热力图
# plt.subplot(413)
# plt.plot(filter_banks)

plt.subplot(414)
plt.plot(mfcc)
plt.show()