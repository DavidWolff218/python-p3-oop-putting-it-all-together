#!/usr/bin/env python3

from book import Book

import io
import sys
import unittest
from unittest.mock import MagicMock


class TestBook(unittest.TestCase):
    '''Book in book.py'''

    def test_initialize_with_title(self):
        '''gets initialized with a title.'''
        mock_page_count = MagicMock()
        mock_page_count.get_page_count.return_value = None
        book = Book("And Then There Were None", mock_page_count)
        self.assertEqual(book.title, "And Then There Were None")
       

    def test_has_title(self):
        '''has the title passed into __init__.'''
        book = Book("And Then There Were None")
        assert(book.title == "And Then There Were None")
        

    def test_has_author_name(self):
        '''can be assigned an author name.'''
        book = Book("And Then There Were None")
        book.author = "Agatha Christie"
        assert(book.author == "Agatha Christie")

    def test_has_page_count(self):
        '''can be assigned a page count property.'''
        book = Book("And Then There Were None", 0)
        book.page_count = 272
        assert book.page_count == 272

    def test_requires_int_page_count(self):
        '''prints "page_count must be an integer" if page_count is not an integer.'''
        book = Book("And Then There Were None")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.page_count = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "page_count must be an integer\n"
        assert not book.page_count

    def test_has_genre(self):
        '''can be assigned a genre.'''
        book = Book("And Then There Were None")
        book.genre = "Mystery"
        assert(book.genre == "Mystery")

    def test_can_turn_page(self):
        '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''
        book = Book("The World According to Garp")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.turn_page()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Flipping the page...wow, you read fast!\n")
        
        
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestBook('test_initialize_with_title'))
    suite.addTest(TestBook('test_has_title'))
    suite.addTest(TestBook('test_has_author_name'))
    suite.addTest(TestBook('test_has_page_count'))
    suite.addTest(TestBook('test_requires_int_page_count'))
    suite.addTest(TestBook('test_has_genre'))
    suite.addTest(TestBook('test_can_turn_page'))
    unittest.TextTestRunner().run(suite)
