import json
import os


class Library:
    def __init__(self, filename='library.json'):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        """Загрузка книг из файла."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []

    def save_books(self):
        """Сохранение книг в файл."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.books, file, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        """Добавление новой книги."""
        new_id = max([book['id'] for book in self.books], default=0) + 1
        new_book = {
            "id": new_id,
            "title": title,
            "author": author,
            "year": year,
            "status": "в наличии"
        }
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' добавлена.")

    def remove_book(self, book_id):
        """Удаление книги по ID."""
        for book in self.books:
            if book['id'] == book_id:
                self.books.remove(book)
                self.save_books()
                print(f"Книга с ID {book_id} удалена.")
                return
        print(f"Книга с ID {book_id} не найдена.")

    def search_books(self, query):
        """Поиск книг по title, author или year."""
        results = [book for book in self.books if query in book['title'] or query in book['author'] or query in str(book['year'])]
        return results

    def display_books(self):
        """Отображение всех книг."""
        if not self.books:
            print("Библиотека пуста.")
            return
        for book in self.books:
            print(
                f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {book['status']}")

    def update_status(self, book_id, new_status):
        """Изменение статуса книги."""
        for book in self.books:
            if book['id'] == book_id:
                book['status'] = new_status
                self.save_books()
                print(f"Статус книги с ID {book_id} изменен на '{new_status}'.")
                return
        print(f"Книга с ID {book_id} не найдена.")


def main():
    library = Library()

    while True:
        print("\n1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(title, author, year)
        elif choice == '2':
            book_id = int(input("Введите ID книги: "))
            library.remove_book(book_id)
        elif choice == '3':
            query = input("Введите название, автора или год: ")
            results = library.search_books(query)
            if results:
                for book in results:
                    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {book['status']}")
            else:
                print("Книги не найдены.")
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            book_id = int(input("Введите ID книги: "))
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            library.update_status(book_id, new_status)
        elif choice == '6':
            print("Выход.")
            break
        else:
            print("Ошибка, попробуйте снова.")


if __name__ == "__main__":
    main()
