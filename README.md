# converting-string-session

конвертация Telethon `.session` файлов в строковый формат (`StringSession`).  >>> ВКЛЮЧИТЬ ВПН

- Python 3.13+

```bash
poetry install
```

Создать файл `.env` в корне проекта:

```env
API_ID=1234567
API_HASH=your_api_hash_here
```
Положить `.session` файлы в `files/files_to_convert/`:

   ```
   files/files_to_convert/
   └── 258815430_telethon.session
   ```
Запуск:

   ```bash
   poetry run python src/convert.py
   ```

Результат в `files/ready/ready.py`:

   ```python
   SESSIONS = {
       '12345678_telethon': '1BVtsOK4Bu...',
   }
   ```

## Структура проекта

```
.
├── .env                         
├── pyproject.toml
├── poetry.lock
├── files/
│   ├── files_to_convert/      
│   └── ready/
│       └── ready.py              # генерируется автоматически
└── src/
    └── convert.py
```
