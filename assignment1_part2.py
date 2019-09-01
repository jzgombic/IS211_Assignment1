#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Book(object):
    
    author = " "

    title = " "

    def __init__(self, author, title):
        """A function that takes in an author and a title,
        and sets them to the object variables.

        Args:
            author (str): The author of the book.
            title (str): The title of the book.

        Attributes:
            author (str): The author of the book.
            title (str): The title of the book.

        """

        self.author = author
        self.title = title

    def display(self):
        
        book = '"{}, written by {}"'.format(self.title, self.author)
        print(book)

BOOK_1 = Book('John Steinbeck', 'Of Mice and Men')

BOOK_2 = Book('Harper Lee', 'To Kill a Mockingbird')

BOOK_1.display()
BOOK_2.display()
