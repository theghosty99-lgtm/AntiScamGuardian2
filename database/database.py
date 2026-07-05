import os
import sqlite3

DB_PATH = "database/guild.db"

# Create the database folder if it doesn't exist
os.makedirs("database", exist_ok=True)


def init_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ---------------- Guild Settings ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS guild_settings(
        guild_id INTEGER PRIMARY KEY,
        log_channel INTEGER,
        auto_delete INTEGER DEFAULT 1,
        auto_timeout INTEGER DEFAULT 0,
        ocr_enabled INTEGER DEFAULT 1,
        qr_enabled INTEGER DEFAULT 1,
        url_enabled INTEGER DEFAULT 1
    )
    """)

    # ---------------- Role Whitelist ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS role_whitelist(
        guild_id INTEGER,
        role_id INTEGER,
        PRIMARY KEY (guild_id, role_id)
    )
    """)

    # ---------------- User Whitelist ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_whitelist(
        guild_id INTEGER,
        user_id INTEGER,
        PRIMARY KEY (guild_id, user_id)
    )
    """)

    # ---------------- Channel Whitelist ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS channel_whitelist(
        guild_id INTEGER,
        channel_id INTEGER,
        PRIMARY KEY (guild_id, channel_id)
    )
    """)

    conn.commit()
    conn.close()


# =====================================================
# ROLE WHITELIST
# =====================================================

def add_role(guild_id: int, role_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT OR IGNORE INTO role_whitelist (guild_id, role_id) VALUES (?, ?)",
            (guild_id, role_id)
        )


def remove_role(guild_id: int, role_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "DELETE FROM role_whitelist WHERE guild_id = ? AND role_id = ?",
            (guild_id, role_id)
        )


def get_roles(guild_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(
            "SELECT role_id FROM role_whitelist WHERE guild_id = ?",
            (guild_id,)
        ).fetchall()

    return [row[0] for row in rows]


# =====================================================
# USER WHITELIST
# =====================================================

def add_user(guild_id: int, user_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT OR IGNORE INTO user_whitelist (guild_id, user_id) VALUES (?, ?)",
            (guild_id, user_id)
        )


def remove_user(guild_id: int, user_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "DELETE FROM user_whitelist WHERE guild_id = ? AND user_id = ?",
            (guild_id, user_id)
        )


def get_users(guild_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(
            "SELECT user_id FROM user_whitelist WHERE guild_id = ?",
            (guild_id,)
        ).fetchall()

    return [row[0] for row in rows]


# =====================================================
# CHANNEL WHITELIST
# =====================================================

def add_channel(guild_id: int, channel_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT OR IGNORE INTO channel_whitelist (guild_id, channel_id) VALUES (?, ?)",
            (guild_id, channel_id)
        )


def remove_channel(guild_id: int, channel_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "DELETE FROM channel_whitelist WHERE guild_id = ? AND channel_id = ?",
            (guild_id, channel_id)
        )


def get_channels(guild_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(
            "SELECT channel_id FROM channel_whitelist WHERE guild_id = ?",
            (guild_id,)
        ).fetchall()

    return [row[0] for row in rows]


# =====================================================
# GUILD SETTINGS
# =====================================================

def create_guild(guild_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT OR IGNORE INTO guild_settings (guild_id) VALUES (?)",
            (guild_id,)
        )


def get_settings(guild_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute(
            "SELECT * FROM guild_settings WHERE guild_id = ?",
            (guild_id,)
        ).fetchone()

    return row


def set_log_channel(guild_id: int, channel_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "UPDATE guild_settings SET log_channel = ? WHERE guild_id = ?",
            (channel_id, guild_id)
        )