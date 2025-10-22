Caesar Cipher Learning Pack
================================

A hands-on set of Python scripts for teaching and experimenting with the classic Caesar cipher. The project walks learners from alphabet visualizations all the way to a simple interactive sandbox.  
> **Disclaimer:** This content is strictly educational and not intended for real cryptographic use.

![Kapture 2025-10-21 at 22 08 40](https://github.com/user-attachments/assets/4e91df38-ec17-4236-91f1-705ca67bf7e0)



Repository Layout
-----------------
```
.
├── README.md
├── updates.md                 # Packaging & roadmap notes
└── src/
    ├── __init__.py
    ├── caesar_educational.py  # Beginner-friendly walkthrough
    ├── letter_mapping.py      # Alphabet rotation visualizer
    ├── caesar_cipher.py       # Intermediate implementation
    ├── interactive_demo.py    # Interactive encode/decode loop
    └── caesar_qt_app.py       # Optional PyQt6 desktop app
```

Quick Start
-----------
**Prerequisites:** Python 3.8 or newer. A virtual environment is recommended (`python -m venv .venv && source .venv/bin/activate`).

1. Clone the repository.
2. (Optional) Activate your virtual environment.
   - Install extras as needed, e.g. `pip install PyQt6` to launch the GUI.
3. Run any script with Python 3.8+:
   ```bash
   python -m src.caesar_educational
   python -m src.letter_mapping
   python -m src.caesar_cipher
   python -m src.interactive_demo
   # Optional PyQt6 GUI (pip install PyQt6 first)
   python -m src.caesar_qt_app
   ```

Sample Interactive Run
----------------------
```bash
$ python -m src.interactive_demo
Enter text to encode: hello world
Enter shift (1–25): 5
Type 'd' to decode, Type 'e' encode, or 'q' to quit: e

--- Interactive Result ---
Result: mjqqt btwqi
```

Choose Your Path
----------------
- **Beginner – `src/caesar_educational.py`**  
  Prints the full mapping for each shift, highlights lowercase/uppercase handling, and shows example encode/decode flows.
- **Visualization – `src/letter_mapping.py`**  
  Demonstrates alphabet rotation using both `zip()` pairing and manual index loops to reinforce how substitution ciphers work.
- **Intermediate – `src/caesar_cipher.py`**  
  Focuses on the core `caesar()` helper with concise validation and demonstrations of encode/decode helper functions.
- **Sandbox – `src/interactive_demo.py`**  
  Provides an infinite loop where learners can choose encode or decode, pick shift values, and experiment with their own phrases.
- **GUI – `src/caesar_qt_app.py`**  
  PyQt6 desktop application with live encode/decode preview, alphabet mapping grid, ROT13 shortcut, and history panel (install PyQt6 to launch).

Educational Highlights
----------------------
- Comments explain the **why** alongside the **what** so learners can follow reasoning.
- Examples show both lowercase and uppercase handling plus non-letter preservation.
- The interactive demo encourages experimentation without restarting the script.

What You’ll Learn
-----------------
- How substitution ciphers rotate alphabets and why valid shifts are 1–25.
- Using Python’s `str.maketrans()` and `str.translate()` to build mapping tables.
- Structuring helper functions (`encode_msg`, `decode_msg`) for clarity.
- Building simple command-line loops and validating user input.

Where to Go Next
----------------
- The forward-looking roadmap and packaging plan live in `updates.md`.
- Future work includes a polished CLI package (pip/pipx installable) and optional Homebrew wrapper as described in that document.
- Contributions, suggestions, or classroom adaptations are welcome—feel free to open an issue or fork the repository.

Further Reading
---------------
- [Python `str.translate` documentation](https://docs.python.org/3/library/stdtypes.html#str.translate)
- [Python `str.maketrans` documentation](https://docs.python.org/3/library/stdtypes.html#str.maketrans)
- [An introduction to substitution ciphers](https://en.wikipedia.org/wiki/Substitution_cipher)
- [GeeksforGeeks: Caesar Cipher in Cryptography](https://www.geeksforgeeks.org/ethical-hacking/caesar-cipher-in-cryptography/)
- [FreeCodeCamp Caesar Cipher Workshop](https://www.freecodecamp.org/learn/full-stack-developer/workshop-caesar-cipher/step-1)
- [YouTube: Caesar Cipher Explained](https://www.youtube.com/watch?v=sMOZf4GN3oc)

License
-------
Licensed under the MIT License. See `LICENSE` (to be added) for details.
