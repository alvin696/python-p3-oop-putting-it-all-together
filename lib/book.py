#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None
        self.page_count = page_count
        self.borrowed = False

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, count):
        if isinstance(count, int):
            self._page_count = count
        else:
            print("page_count must be an integer")

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return True
        else:
            return False

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return True
        else:
            return False

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
