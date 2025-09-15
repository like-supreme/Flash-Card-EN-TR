# Flash-Card-EN-TR
A minimal Tkinter-based English → Turkish flash card application. Words are loaded from a CSV file, each card automatically flips after 2.5 seconds, and progress is tracked locally. When you mark a word as “✅ learned,” it’s removed from the pool and saved to a CSV file.  The project is simple, file-based, and easily customizable.

Flash Cards (EN → TR) — Tkinter

A simple desktop application for memorizing vocabulary quickly.
Each flash card shows an English word on the front, then flips to show the Turkish translation after 2.5 seconds.
When you press ✅ Learned, the word is removed from the pool and your progress is saved.
This version only uses turkish_words.csv (the French dataset was removed).

Features

CSV-based data model: Reads from data/turkish_words.csv automatically.

Timed card flipping: Uses Tkinter after to flip after 2.5 seconds.

Progress tracking: Learned words are removed and written to a local CSV file (learnedwords.csv in the current code).

Clean UI: Large fonts, front/back card images, and ✅/❌ buttons.

images/
  card_back.png
  card_front.png
  right.png
  wrong.png
  data/
    turkish_words.csv
  notes/
    notes.txt
  main.py
  
Installation
1) Clone the repo
git clone <repo-url>
cd <repo-folder>

2) Create a virtual environment (recommended)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

3) Install dependencies
pip install -r requirements.txt


On Linux you may need python3-tk:

sudo apt-get install python3-tk

Run the app
python src/main.py

Suggested Project Structure
.
├─ src/
│  └─ main.py
├─ data/
│  └─ turkish_words.csv
├─ images/
│  ├─ card_back.png
│  ├─ card_front.png
│  ├─ right.png
│  └─ wrong.png
├─ README.md
├─ requirements.txt
└─ .gitignore

How it Works

Loading data: turkish_words.csv is loaded into memory as a list of word pairs.

Random card selection: A random English word is displayed.

Flip timer: After 2.5 seconds the card flips to reveal the Turkish translation.

✅ Learned: Removes the card from the list, writes progress to a CSV file, and moves on.

❌ Wrong: Moves to the next card without removing it.

Customization

Flip time: Change window.after(2500, flip_card) to adjust the delay.

Theme: Edit BACKGROUND_COLOR, fonts, and image assets.

Dataset: Replace contents of turkish_words.csv (keep headers English,Turkish).

Tkinter comes bundled with Python (except on Linux, where python3-tk is required).

Future Improvements

Replace absolute paths with relative paths (Pathlib) for cross-platform support.

Avoid recursion for error handling; prefer one-time message + return.

Refactor to an OOP class-based structure (FlashCardApp) for cleaner code.
