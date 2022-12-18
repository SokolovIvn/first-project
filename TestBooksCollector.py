from BooksCollector import BooksCollector


class TestBooksCollector:

    def test_add_new_book_book_name_true(self, book_name):  # добавили новую книгу и проверили имя
        books = BooksCollector()
        books.add_new_book(name=book_name)
        assert_book = list(books.books_rating.keys())
        assert assert_book[0] == book_name

    def test_get_book_rating_default_rating_true(self, book_name):  # протестировать дефолтный рейтинг у добавленной книги по имени книги
        books = BooksCollector()
        books.add_new_book(name=book_name)
        assert books.get_book_rating(book_name) == 1

    def test_get_book_rating_set_custom_rating_true(self, book_name):  # проверка установки кастомного рейтинга
        custom_rating = 3
        books = BooksCollector()
        books.add_new_book(name=book_name)
        books.set_book_rating(book_name, custom_rating)
        assert books.get_book_rating(book_name) == custom_rating

    def test_get_book_specific_rating_set_some_rating_true(self, book_name):  # проверка вывода книги с определенным рейтингом
        custom_rating = 3
        books = BooksCollector()
        books.add_new_book(name=book_name)
        books.set_book_rating(book_name, custom_rating)
        books.get_books_with_specific_rating(custom_rating)
        assert books.get_book_rating(book_name) == custom_rating

    def test_get_books_rating_type_dict_true(self, book_name):  # проверяем что это словарь
        books = BooksCollector()
        books.add_new_book(name=book_name)
        books.get_books_rating()
        assert type(books.get_books_rating()) == dict

    def test_get_books_rating_check_equal_books_true(self, book_name):  # проверяем кол-во записей в словаре
        books = BooksCollector()
        books.add_new_book(name=book_name)
        books.add_new_book(name='book2')
        books.get_books_rating()
        assert len(books.get_books_rating()) == 2

    def test_add_book_in_favorites_check_favourite_books_true(self, book_name):  # проверяем, что книга в избранном
        books = BooksCollector()
        books.add_new_book(name=book_name)
        books.add_book_in_favorites(book_name)
        assert book_name in books.get_list_of_favorites_books()

    def test_delete_book_from_favorites_check_del_favourite_book_true(self, book_name):  # проверяем, что книга удалена из избранного
        books = BooksCollector()
        books.add_new_book(name=book_name)
        books.add_book_in_favorites(book_name)
        books.delete_book_from_favorites(book_name)
        aaa = books.get_list_of_favorites_books()
        assert book_name not in aaa

    def test_get_list_of_favorites_books_check_favourite_books_true(self, book_name):  # проверяем список с избранным
        books = BooksCollector()
        books.add_new_book(name=book_name)
        books.add_new_book(name='book_name2')
        books.add_book_in_favorites(book_name)
        assert book_name in books.get_list_of_favorites_books()
