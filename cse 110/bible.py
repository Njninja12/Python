


choice = input("What volume of scripture would you like to choose? ")

max_chapter = -1
max_book = ""

with open("books_and_chapters.txt") as bible_books:
    for line in bible_books:
        parts = line.split(":")
        book = parts[0].strip()
        chapter = int(parts[1])
        scripture = parts[2].strip()



        if scripture.lower() == choice.lower():


            print(f"Scripture: {scripture}, Book: {book}, Chapter: {chapter}")


            if chapter > max_chapter:
            # This book is the new best one!
                max_chapter = chapter # The max chapters is now this one
                max_book = book # Remember the name of the book

# This is now after the loop has finished
print(f"\n\nThe book with the most chapters is: {max_book}")
print(f"It has {max_chapter} chapters.")