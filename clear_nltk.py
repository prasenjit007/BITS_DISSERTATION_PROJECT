import shutil
import os

nltk_data_path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "nltk_data")
if os.path.exists(nltk_data_path):
    shutil.rmtree(nltk_data_path)
    print("Deleted corrupted nltk_data folder.")
else:
    print("No corrupted nltk_data found.")
