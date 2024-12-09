# **Python Keylogger**

This is a simple Python-based keylogger that logs keystrokes with timestamps and detects specific key sequences. The project is for **educational purposes only** and demonstrates fundamental concepts in cybersecurity and Python programming.

---

## **Features**
1. **Keystroke Logging**: Captures all keystrokes, including special keys (e.g., Space, Enter, etc.).
2. **Time-Stamped Logs**: Logs each keystroke along with the exact date and time it was pressed.
3. **Special Sequence Detection**: Detects predefined key sequences, such as:
   - `Ctrl + Alt + Delete`
   - "password123"
   - Custom sequences can also be added.
4. **Clean Termination**: Safely stops the logger with `Ctrl + C` and saves the logs to a file.

---

## **Requirements**
- Python 3.x
- Libraries:
  - `pynput`: To capture keystrokes.
  - `datetime`: For adding timestamps.

---

## **Installation**
1. Clone or download the repository:
   ```bash
   git clone https://github.com/your-repo/keylogger.git
   cd keylogger
   ```
2. Set up a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install the required libraries:
   ```bash
   pip install pynput
   ```

---

## **Usage**
1. Run the keylogger:
   ```bash
   python keylogger.py
   ```
2. Press keys on your keyboard. 
   - Keystrokes will be logged in the `keylog.txt` file.
   - If a predefined key sequence is detected, an alert will appear in the terminal.

3. Stop the keylogger with `Ctrl + C`.

---

## **File Structure**
- `keylogger.py`: Main script for the keylogger.
- `keylog.txt`: Log file where all keystrokes and timestamps are saved.

---

## **Customization**
### Add Your Own Key Sequences
1. Open the `keylogger.py` file.
2. Modify the `key_sequences` list to include the sequences you want to detect. Example:
   ```python
   key_sequences = [
       ['Key.ctrl_l', 'Key.alt_l', 'Key.delete'],  # Detect Ctrl+Alt+Delete
       ['s', 'e', 'c', 'u', 'r', 'i', 't', 'y'],  # Detect "security"
   ]
   ```

---

## **Sample Log File**
Example `keylog.txt`:
```
2024-12-09 12:15:10 - H
2024-12-09 12:15:11 - e
2024-12-09 12:15:12 - l
2024-12-09 12:15:12 - l
2024-12-09 12:15:13 - o
2024-12-09 12:15:14 - SPACE
2024-12-09 12:15:15 - [Key.enter]
```
