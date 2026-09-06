import os
import glob
import csv

# Jahan tera data folder hai (isme female aur male subfolders hain)
data_dir = "data"

# Output CSV file ka naam
output_csv = "metadata.csv"

# Sabhi .wav files dhundho (recursively, female aur male dono mein)
wav_files = glob.glob(os.path.join(data_dir, "**", "*.wav"), recursive=True)

rows = []
missing_text_count = 0

for wav_path in wav_files:
    # Base name nikaalo (e.g., "188" from "188.wav")
    base_name = os.path.splitext(os.path.basename(wav_path))[0]
    
    # Corresponding .txt file path (same folder mein)
    txt_path = os.path.join(os.path.dirname(wav_path), base_name + ".txt")
    
    # Check karo ki .txt file hai ya nahi
    if not os.path.exists(txt_path):
        missing_text_count += 1
        print(f"⚠️ Warning: No text file found for {os.path.basename(wav_path)}")
        continue
    
    # .txt file padho
    with open(txt_path, 'r', encoding='utf-8') as f:
        text = f.read().strip().replace('\n', ' ')  # Extra newlines hatao
    
    # Speaker name folder se nikaalo
    folder_name = os.path.basename(os.path.dirname(wav_path))
    if "female" in folder_name.lower():
        speaker = "female"
    elif "male" in folder_name.lower():
        speaker = "male"
    else:
        speaker = "unknown"
    
    # Row add karo (sirf filename daal rahe hain, full path nahi)
    rows.append([os.path.basename(wav_path), text, speaker])
    print(f"✅ {os.path.basename(wav_path)} | {speaker} | {text[:30]}...")

# CSV file save karo
with open(output_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='|')
    writer.writerow(["audio_file", "text", "speaker_name"])  # Header
    writer.writerows(rows)

print("\n" + "="*50)
print(f"✅ Done! Total entries: {len(rows)}")
if missing_text_count > 0:
    print(f"⚠️ Missing text files found: {missing_text_count} (ignored)")
else:
    print("🎉 All WAV files have matching TXT files!")
print("="*50)