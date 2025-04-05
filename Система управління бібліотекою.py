class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_borrowed = False

    def borrow_item(self):
        self.is_borrowed = not self.is_borrowed
        return f'"{self.title}" {"Взято" if self.is_borrowed else "Повернено"}.'

    def display_info(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, item_id, pages):
        super().__init__(title, item_id)
        self.pages = pages

    def display_info(self):
        print(f'Книга: {self.title}, {self.pages} ст.')


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def display_info(self):
        print(f'Журнал: {self.title}, Випуск {self.issue_number}')


class Audiobook(LibraryItem):
    def __init__(self, title, item_id, duration):
        super().__init__(title, item_id)
        self.duration = duration

    def display_info(self):
        print(f'Аудіокнига: {self.title}, {self.duration} хв')


library_items = [
    Book("Гаррі Потер", 1, 1300),
    Magazine("Поліанна", 2, 57),
    Audiobook("2000", 3, 790)
]

for item in library_items:
    item.display_info()

