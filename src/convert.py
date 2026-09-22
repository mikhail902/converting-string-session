import os
from pathlib import Path
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

if not api_id or not api_hash:
    raise ValueError("API_ID и API_HASH должны быть заданы в .env")

api_id = int(api_id)

SOURCE_DIR = BASE_DIR / "files" / "files_to_convert"
READY_DIR = BASE_DIR / "files" / "ready"
READY_FILE = READY_DIR / "ready.py"


def convert_session(session_path: Path) -> str | None:
    session_name = str(session_path.with_suffix(""))
    try:
        with TelegramClient(session_name, api_id, api_hash) as client:
            return StringSession.save(client.session)
    except Exception as e:
        print(f"[ОШИБКА] {session_path.name}: {e}")
        return None


def main():
    READY_DIR.mkdir(parents=True, exist_ok=True)

    sessions = sorted(SOURCE_DIR.glob("*.session"))

    if not sessions:
        print(f"В папке {SOURCE_DIR} не найдено .session файлов")
        return

    results = {}
    for session_file in sessions:
        print(f"[+] Обработка: {session_file.name}")
        string_session = convert_session(session_file)
        if string_session:
            results[session_file.stem] = string_session
            print("    OK")

    lines = ["SESSIONS = {"]
    for name, sess in results.items():
        lines.append(f"    {name!r}: {sess!r},")
    lines.append("}")
    lines.append("")

    READY_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n[ГОТОВО] Записано {len(results)} сессий -> {READY_FILE}")


if __name__ == "__main__":
    main()