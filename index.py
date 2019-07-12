import re
import os
import collections
import time

class Index:

    def __init__(self, path):
        self.path = path

    def buildIndex(self):
        # function to read documents from collection, tokenize and build the index with tokens
        # index should also contain positional information of the terms in the
        # document --- term: [(ID1,[pos1,pos2,..]), (ID2, [pos1,pos2,…]),….]
        # use unique document IDs

        # begin timer
        start = time.clock()
        # retrieve all documents from collection directory
        text_files = os.listdir(self.path)
        # text_files = ['Text-001.txt', 'Text-002.txt']
        text_dictionary = {}
        text_id = 1

        for text_file in text_files:
            # concatenate path with file name
            text_file_path = self.path + text_file

            # retrieve contents from file
            text_contents = self.read_text_file(text_file_path)

            # convert string to list
            text_contents = self.convert_string_to_list(text_contents)

            # build dictionary
            text_dictionary = self.build_dictionary(text_id, text_contents, text_dictionary)

            text_id += 1

        # end timer
        end = time.clock()
        total_time = end - start
        return text_dictionary, total_time

    def and_query(self, query_terms):
        # function for identifying relevant docs using the index

        # begin timer
        start = time.clock()

        documents_per_word = {}
        # for every term in query_terms
        for term in query_terms:
            # get the key/value
            for key, value in final_index[0].items():
                # if the term equals the key
                if term == key:
                    # then the first position in each list is the ID of a document holding this value
                    temp = []
                    for arr in value:
                        temp.append(arr[0])
                    if temp:
                        documents_per_word[key] = temp

        # get arbitrary text_id list
        list_of_text_ids_with_all_words = list(documents_per_word.values())[0]
        # for each key/value in documents_per_word
        for key, value in documents_per_word.items():
            # store the intersection of these two lists, and check the intersection of every
            # subsequent list against this list, which will shrink as text_ids are removed
            list_of_text_ids_with_all_words = set(list_of_text_ids_with_all_words).intersection(value)

        # create sentence describing the query
        query_sentence = self.create_query_sentence(query_terms)
        total_docs = len(list_of_text_ids_with_all_words)

        # print results
        print('Results for the query:', query_sentence)
        print('Total docs retrieved:', total_docs)
        for doc in list_of_text_ids_with_all_words:
            print(self.doc_name(doc))

        # end timer
        end = time.clock()
        total_time = end - start
        # print time
        print('Retrieved in', total_time)

    def print_dict(self):
        # function to print the terms and posting list in the index
        index_to_print = self.buildIndex()
        print(index_to_print)

    def print_doc_list(self):
        # function to print the documents and their document id
        # get doc dictionary
        doc_dict = self.get_doc_id_and_title_dict()
        # print each key value pair
        for key, value in doc_dict.items():
            key_string = str(key)
            print(key_string + ' ==> ' + value)

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

    def build_dictionary(self, text_id, word_list, text_dictionary):

        this_dict = text_dictionary
        text = text_id

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

    def create_query_sentence(self, query_terms):
        # create sentence describing the query
        sentence = ''
        for word in query_terms:
            if word == query_terms[0]:
                sentence = word
            else:
                sentence += ' AND ' + word
        return sentence

    def doc_name(self, doc):
        # get doc id dictionary
        doc_dict = self.get_doc_id_and_title_dict()
        for key, value in doc_dict.items():
            # if doc passed in to this function equals the key in the dictionary return the value
            if doc == key:
                return value

    def get_doc_id_and_title_dict(self):
        # get all text files
        text_files = os.listdir(self.path)
        # create empty list and iterator
        doc_dict = {}
        i = 1
        # cast int to string, concatenate, and append to list
        for text_file in text_files:
            doc_dict[i] = text_file
            i += 1
        return doc_dict


index = Index('collection/')
final_index = index.buildIndex()
# print(final_index)
# print('Index built in', final_index[1], 'seconds')
#
index.and_query(['with', 'had', 'the', 'was'])
index.and_query(['china', 'that'])
index.and_query(['would', 'end', 'the', 'war'])
index.and_query(['hat', 'time', 'put'])
index.and_query(['practice', 'banker', 'program', 'operation', 'employee', 'government'])
# index.print_doc_list()
