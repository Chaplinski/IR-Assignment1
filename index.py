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
        # text_files = os.listdir("collection/")
        text_files = ['Text-001.txt', 'Text-002.txt']
        text_dictionary = {}

        for text_file in text_files:

            text_file_path = "collection/" + text_file

            # retrieve contents from file
            text_contents = self.read_text_file(text_file_path)

            # convert string to list
            text_contents = self.convert_string_to_list(text_contents)

            # build dictionary
            text_dictionary = self.build_dictionary(text_file, text_contents, text_dictionary)

            # alphabetize dictionary
            # text_dictionary = collections.OrderedDict(sorted(text_dictionary.items()))

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

    def build_dictionary(self, text_title, word_list, text_dictionary):

        this_dict = text_dictionary
        text = text_title

        integer = 0
        # for every word in a text
        for potential_new_word in word_list:
            # check if the word already exists in the dictionary
            if potential_new_word in this_dict:
                # if word does exist then access its value array
                for key, value in this_dict.items():
                    # if the new word being added is the same as a key value
                    if key == potential_new_word:
                        # temp list holds values of all texts that already have int values saved
                        already_saved_texts = []
                        for list in value:
                            # append text name to already_saved_texts list
                            already_saved_texts.append(list[0])
                        # set Boolean to false as a default
                        is_already_saved = False
                        # iterate though already_saved_texts looking for current text
                        for text_val in already_saved_texts:
                            # if current text exists set Boolean to true
                            if text_val == text:
                                is_already_saved = True

                        # if text already has values saved
                        if is_already_saved:
                            # iterate through lists
                            for list in value:
                                # position 0 in a list refers to the definition of what text it refers to
                                if list[0] == text:
                                    # if first value in key list is a text that already has this term then append
                                    # word int location to list
                                    list[1].append(integer)
                        # if list does not already have values saved
                        else:
                            # append text and word int location to list
                            value.append([text, [integer]])

            else:
                # if word does not already exist in dictionary
                # create new list containing text ID and int position in text to become value of new key
                new_list = [text, [integer]]
                # update dictionary to hold new key/value
                this_dict.update({potential_new_word: [new_list]})

            integer += 1

        return this_dict
