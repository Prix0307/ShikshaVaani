import os
import subprocess
from glob import glob

data_dir = "data"
output_dir = "data_converted"

# Female aur male folders create karo
for folder in ["female", "male"]:
    os.makedirs(os.path.join(output_dir, folder), exist_ok=True)

# Saari .wav files dhundho
wav_files = glob(os.path.join(data_dir, "**", "*.wav"), recursive=True)

for wav_path in wav_files:
    # Folder aur filename nikaalo
    folder = os.path.basename(os.path.dirname(wav_path))  # "female" or "male"
    filename = os.path.basename(wav_path)
    
    # Output path
    out_path = os.path.join(output_dir, folder, filename)
    
    # ffmpeg command
    cmd = [
        "ffmpeg", "-i", wav_path,
        "-ar", "16000", "-ac", "1",
        out_path
    ]
    
    print(f"Converting: {wav_path} -> {out_path}")
    subprocess.run(cmd, check=True, capture_output=True)

print("✅ All files converted successfully!")