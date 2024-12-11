import wave
import numpy as np
import os

# Define the input and output wav file paths
current_path = os.path.dirname(os.path.abspath(__file__))


inputFile = os.path.join(current_path, 'salt', '0_VO_000080_(0).wav')
outputFile = os.path.join(current_path, 'output.wav')

# Cut the wav file from start_time to end_time
def cut_wav(input_wav, output_wav, start_time, end_time):
    # Open the input file
    with wave.open(input_wav, 'rb') as f:
        params = f.getparams()
        nchannels, sampwidth, framerate, nframes = params[:4]
        str_data = f.readframes(nframes)
    wave_data = np.frombuffer(str_data, dtype=np.short)
    wave_data.shape = -1, nchannels
    wave_data = wave_data.T

    # Convert start_time and end_time to integer frame indices
    start_frame = int(start_time * framerate)
    end_frame = int(end_time * framerate)

    new_nframes = end_frame - start_frame

    # Open the output file
    with wave.open(output_wav, 'wb') as f:
        f.setnchannels(nchannels)
        f.setsampwidth(sampwidth)
        f.setframerate(framerate)
        f.setnframes(new_nframes)
        f.writeframes(wave_data.T[start_frame:end_frame].tobytes())

if __name__ == '__main__':
    cut_wav(inputFile, outputFile, 0, 0.33333)