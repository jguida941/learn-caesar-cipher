Caesar Cipher Learning Pack
================================

A hands-on set of Python scripts for teaching and experimenting with the classic Caesar cipher. The project walks learners from alphabet visualizations all the way to a simple interactive sandbox.  
> **Disclaimer:** This content is strictly educational and not intended for real cryptographic use.

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
    └── interactive_demo.py    # Interactive encode/decode loop
```

Quick Start
-----------
1. Optional: activate a virtual environment (`python -m venv .venv && source .venv/bin/activate`).
2. Run any script with Python 3.8+:
   ```bash
   python -m src.caesar_educational
   python -m src.letter_mapping
   python -m src.caesar_cipher
   python -m src.interactive_demo
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

Educational Highlights
----------------------
- Comments explain the **why** alongside the **what** so learners can follow reasoning.
- Examples show both lowercase and uppercase handling plus non-letter preservation.
- The interactive demo encourages experimentation without restarting the script.

Where to Go Next
----------------
- The forward-looking roadmap and packaging plan live in `updates.md`.
- Future work includes a polished CLI package (pip/pipx installable) and optional Homebrew wrapper as described in that document.
- Contributions, suggestions, or classroom adaptations are welcome—feel free to open an issue or fork the repository.

License
-------
Licensed under the MIT License. See `LICENSE` (to be added) for details.
