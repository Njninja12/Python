with open("books.txt") as book_list:
    for lines in book_list:
        books = lines.strip()

        print(books)