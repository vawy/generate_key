notes = [
    {
        "username": "Вова",
        "title": "Учёба",
        "content": "Подготовка к экзамену",
        "status": "активна",
        "created_date": "10-11-2023",
        "issue_date": "15-11-2023"
    },
    {
        "username": "Маша",
        "title": "Работа",
        "content": "Подготовка отчёта",
        "status": "завершена",
        "created_date": "05-11-2023",
        "issue_date": "10-11-2023"
    }
]

def save_notes_to_file(notes: list[dict], filename):
    """
    Записывает список заметок в текстовый файл, перезаписывая его содержимое.
    """
    try:
        # Открываем файл в режиме записи ('w')
        with open(filename, 'w', encoding='utf-8') as file:
            for note in notes:
                # Записываем каждую заметку в файл
                file.write(f"Имя пользователя: {note.get('username', 'N/A')}\n")
                file.write(f"Заголовок: {note.get('title', 'N/A')}\n")
                file.write(f"Описание: {note.get('content', 'N/A')}\n")
                file.write(f"Статус: {note.get('status', 'N/A')}\n")
                file.write(f"Дата создания: {note.get('created_date', 'N/A')}\n")
                file.write(f"Дедлайн: {note.get('issue_date', 'N/A')}\n")
                file.write("\n")  # Пустая строка между заметками
        print(f"Заметки успешно сохранены в файл {filename}!")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

# Сохраняем заметки в файл
save_notes_to_file(notes, "notes.txt")