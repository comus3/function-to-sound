# WAV Generator

This Git repository contains code for a simple WAV file generator. The code allows you to create WAV files with customizable parameters such as frequency and duration of a waveform. It also includes a graphical user interface (GUI) built with Tkinter for ease of use.

## Code Overview

The code is written in Python and relies on several libraries:

- `numpy` for numerical operations.
- `math` for mathematical functions.
- `scipy.io.wavfile` for writing WAV files.
- `tkinter` for creating the graphical user interface.

### Function to Generate WAV Files

The core functionality of this code is provided by the `generateWav` function. Here's an overview of its parameters:

- `func`: A function that defines the waveform to be generated.
- `frequency`: The frequency of the waveform in radians per second.
- `duration`: The duration of the waveform in seconds.
- `sample_rate`: The sample rate for the WAV file (default is 44100 Hz).
- `amplitude`: The amplitude of the waveform (default is 1.0).
- `output_file`: The name of the output WAV file (default is "output.wav").

### Example Usage

The main part of the code demonstrates an example usage of the `generateWav` function. It generates a sine wave over the interval [0, 2π] for 3 seconds and saves it as "output.wav". You can replace this example with your own custom waveform and parameters.

### GUI Interface

Additionally, the code provides a user-friendly GUI using Tkinter. It allows you to input the desired frequency and duration for the waveform and generate the corresponding WAV file by clicking the "Generate WAV" button.

## Getting Started

To use this code and GUI:

1. Clone this Git repository to your local machine.
2. Ensure you have Python installed, along with the required libraries (`numpy`, `scipy`, `tkinter`).
3. Run the script, and the GUI will appear, allowing you to generate custom WAV files.

## Usage Example

Here's an example of how to use the GUI to generate a custom WAV file:

1. Enter the desired frequency (0 to 10 000 Hz) and duration (0 to 60 seconds) in their respective input fields.
2. Click the "Generate WAV" button.
3. If valid parameters are entered, a WAV file will be generated, and a success message will be displayed. The WAV file will be saved as "output.wav" in the same directory as the script.
4. If invalid parameters are entered, an error message will be displayed.

## Contribution

Feel free to contribute to this project by enhancing the code, adding features, or improving the GUI. If you encounter any issues, please report them in the repository's issue tracker.

Happy WAV file generation!