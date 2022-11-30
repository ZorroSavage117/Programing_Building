# page start
print()

# varaibles
books = []
mormon = []
main = ""
main_in = ""
main_li = []
book = ""
chapter = 0
large_chapter = 0

# main code
with open("books_and_chapters.txt") as books_chapters:
    for line in books_chapters:
        info = line.split(":")
        books.append(info)

# first out put
for item in books:
    main = item[2]
    book = item[0]
    chapter = int(item[1])
    print(f"Scripture: {main}, Book: {book}, Chapters: {chapter}")

# page set up
print()

# largest chapter count and the book
for item in books:
    chapter = int(item[1])

    if chapter > large_chapter:
        large_chapter = chapter

        large_book = item[0]

print(f"Biggest chapter count: {large_chapter}, Book: {large_book}")

# page set up
print()

# strech calleges
# only morom
for item in books:
    main = item[2]

    if main == "Book of Mormon":
        mormon.append(item)

for item in books:
    main = item[2]
    book = item[0]
    chapter = int(item[1])
    print(f"Scripture: {main}, Book: {book}, Chapters: {chapter}")

# page set up
print()

# only mormon large chapter
chapter = 0
for item in mormon:
    chapter = int(item[1])

    if chapter > large_chapter:
        large_chapter = chapter

        large_book = item[0]

print(f"Biggest chapter count: {large_chapter}, Book: {large_book}")

# page set up
print()

# input for which main
main_in = input(
    "Which volume of scripture(Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price)? ")
main_in = main_in.lower()
# output for which main
for item in books:
    main = item[2]
    main = main.lower()

    if main == main_in:
        main_li.append(item)

# large chapter for input
chapter = 0
for item in main_li:
    chapter = int(item[1])

    if chapter > large_chapter:
        large_chapter = chapter

        large_book = item[0]

print(f"Biggest chapter count: {large_chapter}, Book: {large_book}")

# page end
print()
