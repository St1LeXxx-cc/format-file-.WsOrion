class CustomFileHandler:
    def __init__(self, file_extension):
        self.file_extension = file_extension

    def save_text(self, text, file_name):
        file_name_with_extension = f"{file_name}{self.file_extension}"
        with open(file_name_with_extension, "w") as file:
            file.write(text)
        print(f"Текст сохранен в файл: {file_name_with_extension}")

    def read_text(self, file_name):
        file_name_with_extension = f"{file_name}{self.file_extension}"
        try:
            with open(file_name_with_extension, "r") as file:
                content = file.read()
            print(f"Текст из файла {file_name_with_extension}:")
            print(content)
        except FileNotFoundError:
            print(f"Файл {file_name_with_extension} не найден!")

# Пример использования
if __name__ == "__main__":
    handler = CustomFileHandler(".WsOrion")
    
    print("Что вы хотите сделать?")
    print("1. Сохранить текст")
    print("2. Прочитать текст")
    choice = input("Выберите опцию (1 или 2): ")

    if choice == "1":
        text = input("Введите текст для сохранения: ")
        file_name = input("Введите имя файла (без расширения): ")
        handler.save_text(text, file_name)
    elif choice == "2":
        file_name = input("Введите имя файла (без расширения) для чтения: ")
        handler.read_text(file_name)
    else:
        print("Некорректный выбор!")
