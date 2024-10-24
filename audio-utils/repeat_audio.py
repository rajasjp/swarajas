import sys
from pydub import AudioSegment

def repeat_audio(input_file_path, repeat_count, output_file_path, silence_duration=5):
    """
    Generate an audio file by repeating the input audio file for a specified number of times,
    with an optional gap of silence between repetitions.

    :param input_file_path: Path of the input audio file
    :param repeat_count: Number of times to repeat the audio
    :param output_file_path: Path where the output audio file should be saved
    :param silence_duration: Duration of silence between repetitions in milliseconds (default is 0)
    """
    # Load the audio file
    audio = AudioSegment.from_file(input_file_path)
    
    # Generate silence of the specified duration
    silence = AudioSegment.silent(duration=silence_duration * 1000)
    
    # Repeat the audio with the specified gap
    repeated_audio = audio
    for _ in range(1, repeat_count):
        repeated_audio += silence+ audio
    
    # Export the repeated audio to a new file
    repeated_audio.export(output_file_path, format="mp3")
    print(f"Output audio file saved as {output_file_path}")

# Example usage
input_path = sys.argv[1]
output_path = sys.argv[2] if len(sys.argv) > 2 else "output.mp3"  # Default output file name
repeat_times = int(sys.argv[3]) if len(sys.argv) > 2 else 5  # Default to 5 repetitions if not provided
silence_gap_duration = int(sys.argv[4]) if len(sys.argv) > 3 else 3  # Default to 3 seconds if not provided

repeat_audio(input_path, repeat_times, output_path, silence_gap_duration)

# Sample command to run the script:
# python repeat_audio.py input.mp3 output.mp3 5 3
