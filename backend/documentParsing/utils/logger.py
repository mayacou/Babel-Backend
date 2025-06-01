# utils/logger.py

import datetime

def log_info(message):
    print(f"[INFO] {timestamp()} {message}")

def log_success(message):
    print(f"[✅ SUCCESS] {timestamp()} {message}")

def log_warning(message):
    print(f"[⚠️ WARNING] {timestamp()} {message}")

def log_error(message):
    print(f"[❌ ERROR] {timestamp()} {message}")

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
