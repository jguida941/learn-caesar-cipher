Caesar Cipher Learning Pack
================================

A hands-on educational Python demo built to teach others the Caesar cipher, focusing on clean structure, readable code, and interactive learning.

A set of Python scripts that teach the Caesar cipher step-by-step—from visualizing the alphabet shift to building and interacting with a full cipher program.

File Overview
-------------
```
.
├── README.md
└── src/
    ├── __init__.py
    ├── caesar_cipher.py
    ├── caesar_educational.py
    ├── interactive_demo.py
    └── letter_mapping.py
```

Learning Path
-------------
- **Start here – `src/caesar_educational.py`**  
  Prints the full alphabet mapping and walks through encode/decode so beginners can see every step. Includes a small interactive prompt.
- **Reinforce the concept – `src/letter_mapping.py`**  
  Visualizes alphabet rotation using both `zip()` and a manual loop, showing exactly how each letter pairs with its shifted partner.
- **Level up – `src/caesar_cipher.py`**  
  A cleaner, intermediate-level implementation focused on the core cipher logic. Demonstrates simple encode/decode examples at the bottom.
- **Experiment – `src/interactive_demo.py`**  
  A looping CLI sandbox that lets you encode, decode, or quit. Type your own messages and choose the shift value each time.

Running the Scripts
-------------------
All files run with standard Python 3. Activate your virtual environment if you use one:

```bash
source .venv/bin/activate  # optional
python -m src.caesar_educational
python -m src.letter_mapping
python -m src.caesar_cipher
python -m src.interactive_demo
```

Next Steps
----------
Tweak the strings, expand the alphabet, or modify the shift logic to explore variants. Each file is self-contained—feel free to experiment without breaking the others.

Instructor Notes
----------------
### Highlights
- Progression: mapping → core cipher → interactive sandbox
- Clarity: comments and docstrings explain why, not just what
- Implementation: uses `str.maketrans()` + `translate()` to preserve case
- Interactivity: input loop lets learners encode/decode repeatedly
