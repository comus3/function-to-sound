import numpy as np
import math
from scipy.io import wavfile
import funcLib

#make wav file
def generateWav(func, frequency, duration, sample_rate=44100, amplitude=1.0, output_file="output.wav"):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = func(t, frequency)
    wavfile.write(output_file, sample_rate, y.astype(np.float32))

def generateWav2(y,sample_rate=44100, output_file="output.wav"):
    wavfile.write(output_file, sample_rate, y.astype(np.float32))

if __name__ == "__main__":
    """
    Exemple d'utilisation : fonction sinusoïdale sur l'intervalle [0, 2*pi] pendant 3 secondes
    func = lambda t: np.sin(t)  # Fonction sinusoïdale
    interval = [0, 2 * np.pi]  # Intervalle de temps
    duration = 3  # Durée en secondes
    generateWav(func, interval, duration, output_file="output.wav")
    """
    func = funcLib.blaster
    #interface
    import tkinter as tk
    from tkinter import messagebox
    def openOutput():
        import os
        os.startfile("output.wav")
    def generateWavButtonClicked():
        try:
            frequency = float(freq_entry.get())
            duration = float(duration_entry.get())
            if 0 <= frequency <= 90000 and 0 <= duration <= 60:
                generateWav(func,frequency, duration)
                messagebox.showinfo("Success", "WAV file generated successfully!")
                openOutput()
                root.quit()
            else:
                messagebox.showerror("Error", "Invalid parameter values. Frequency must be in [0, 10 000] and duration in [0, 60].")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
    root = tk.Tk()
    root.title("WAV Generator")

    freq_label = tk.Label(root, text="Frequency (0 to 90 000):")
    freq_label.pack()
    freq_entry = tk.Entry(root)
    freq_entry.pack()

    duration_label = tk.Label(root, text="Duration (0 to 60 seconds):")
    duration_label.pack()
    duration_entry = tk.Entry(root)
    duration_entry.pack()
    generate_button = tk.Button(root, text="Generate WAV", command=generateWavButtonClicked)
    generate_button.pack()

    root.mainloop()
