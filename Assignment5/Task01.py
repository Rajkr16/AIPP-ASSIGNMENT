import os
import sqlite3
import hashlib
import secrets
import getpass
import datetime
import hmac

# /d:/AIPP/Assignment5/Task01.py
# Simple secure-ish local login system using sqlite + PBKDF2-HMAC
# No hardcoded credentials. Use in local/educational contexts only.


# Configuration
DB_PATH = os.path.join(os.path.dirname(__file__), "users.db")
HASH_NAME = "sha256"
ITERATIONS = 200_000
SALT_SIZE = 16  # bytes


def init_db():
    """Create users table if it doesn't exist."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                salt BLOB NOT NULL,
                pw_hash BLOB NOT NULL,
                iterations INTEGER NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )


def _hash_password(password: str, salt: bytes, iterations: int) -> bytes:
    """Derive a password hash using PBKDF2-HMAC."""
    return hashlib.pbkdf2_hmac(HASH_NAME, password.encode("utf-8"), salt, iterations)


def create_user(username: str, password: str) -> bool:
    """
    Create a new user.
    Returns True on success, False if the username already exists.
    """
    username = username.strip()
    if not username:
        return False

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM users WHERE username = ?", (username,))
        if cur.fetchone():
            return False

        salt = secrets.token_bytes(SALT_SIZE)
        pw_hash = _hash_password(password, salt, ITERATIONS)
        cur.execute(
            "INSERT INTO users (username, salt, pw_hash, iterations, created_at) VALUES (?, ?, ?, ?, ?)",
            (username, sqlite3.Binary(salt), sqlite3.Binary(pw_hash), ITERATIONS, datetime.datetime.utcnow().isoformat()),
        )
        conn.commit()
        return True


def verify_user(username: str, password: str) -> bool:
    """
    Verify username/password. Returns True if credentials are valid.
    Uses constant-time comparison to avoid timing attacks.
    """
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT salt, pw_hash, iterations FROM users WHERE username = ?", (username,))
        row = cur.fetchone()
        if not row:
            # Don't reveal whether the username exists; do a dummy hashing to equalize timing
            _dummy_salt = secrets.token_bytes(SALT_SIZE)
            _ = _hash_password(password, _dummy_salt, ITERATIONS)
            return False

        salt, pw_hash, iterations = row
        # row returns sqlite3.Binary -> bytes
        computed = _hash_password(password, bytes(salt), int(iterations))
        # Use hmac.compare_digest for constant-time comparison
        return hmac.compare_digest(bytes(pw_hash), computed)


def change_password(username: str, old_password: str, new_password: str) -> bool:
    """
    Change a user's password if old_password is valid.
    Returns True on success.
    """
    if not verify_user(username, old_password):
        return False

    salt = secrets.token_bytes(SALT_SIZE)
    pw_hash = _hash_password(new_password, salt, ITERATIONS)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "UPDATE users SET salt = ?, pw_hash = ?, iterations = ? WHERE username = ?",
            (sqlite3.Binary(salt), sqlite3.Binary(pw_hash), ITERATIONS, username),
        )
        conn.commit()
    return True


def cli():
    init_db()
    menu = """
    Choose:
     1) Register
     2) Login
     3) Change password
     4) Exit
    """
    while True:
        print(menu)
        choice = input("Select an option: ").strip()
        if choice == "1":
            username = input("New username: ").strip()
            password = getpass.getpass("New password: ")
            if create_user(username, password):
                print("User created.")
            else:
                print("Failed to create user (maybe exists or invalid username).")
        elif choice == "2":
            username = input("Username: ").strip()
            password = getpass.getpass("Password: ")
            if verify_user(username, password):
                print("Login successful.")
            else:
                print("Login failed.")
        elif choice == "3":
            username = input("Username: ").strip()
            old = getpass.getpass("Current password: ")
            new = getpass.getpass("New password: ")
            if change_password(username, old, new):
                print("Password changed.")
            else:
                print("Password change failed.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    cli()