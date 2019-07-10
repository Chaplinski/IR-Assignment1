import re
import os
import collections
import time

class Index:

    def __init__(self,path):
        self.path = path

    def buildIndex(self):
        # function to read documents from collection, tokenize and build the index with tokens
        # index should also contain positional information of the terms in the
        # document --- term: [(ID1,[pos1,pos2,..]), (ID2, [pos1,pos2,…]),….]
        # use unique document IDs

        # retrieve all documents from collection directory
        text_files = os.listdir("collection/")
        text_dictionary = {}

        for text_file in text_files:

            text_file_path = "collection/" + text_file

            # retrieve contents from file
            text_contents = self.read_text_file(text_file_path)

            # convert string to list
            text_contents = self.convert_string_to_list(text_contents)

            i = 0

            for word in text_contents:
                if not text_dictionary.setdefault(word, []):
                    temp_dictionary = {text_file}
                    text_dictionary.setdefault(word, []).append(temp_dictionary)

                text_dictionary.setdefault(word, []).append(i)
                i += 1

            text_dictionary = collections.OrderedDict(sorted(text_dictionary.items()))

        return text_dictionary

    def and_query(self, query_terms):
        # function for identifying relevant docs using the index
        return query_terms + ' woop'

    def print_dict(self):
        # function to print the terms and posting list in the index
        return 'test'

    def print_doc_list(self):
        # function to print the documents and their document id
        return 'test'

    def read_text_file(self, text_file):
        f = open(text_file, "r")
        contents = f.read()
        return contents

    def convert_string_to_list(self, contents):
        # remove all punctuation and numerals, all text is lowercase
        contents = contents.lower()
        contents = re.sub(r'\d+', '', contents)

        # remove punctuation, replace with a space
        for char in "-:\n":
            contents = contents.replace(char, ' ')

        # remove quotes and apostrophes, replace with empty string
        for char in ".,?!'();$%\"":
            contents = contents.replace(char, '')
        contents = contents.replace('\n', ' ')

        # convert string to list
        contents = contents.split(' ')
        # remove empty strings
        contents = list(filter(None, contents))

        return contents
