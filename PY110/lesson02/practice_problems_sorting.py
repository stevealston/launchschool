lst = [10, 9, -6, 11, 7, -16, 50, 8]

# non-mutating
asc_lst = sorted(lst)
dsc_lst = sorted(lst, reverse=True)

# print(asc_lst)
# print(dsc_lst)

# mutating
lst.sort()
# print(lst)
lst.sort(reverse=True)
# print(lst)

lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort(key=str)
# print(lst)
lst.sort(key=str, reverse=True)
# print(lst)

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]
def by_pub(book):
    return int(book['published'])

books.sort(key=by_pub)
# print(books)
