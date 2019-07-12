This merge algorithm starts by finding the IDs of all of the documents that have each word in 'query_terms'.
It creates a dictionary with each word from the query being a key, and a list of IDs from the documents containing the
word as the value matching that key.

Once the dictionary is complete, we access the first key/value pair in the dictionary. This will always be
different, but that doesn't matter. The algorithm simply needs the value associated with any key to start with.

The variable 'list_of_text_ids_with_all_words' will hold the list from the value of the initial key/value pair.
The intersection() function then takes the list value of each key/value pair in the dictionary and compares it to
'list_of_text_ids_with_all_words'. All values that appear in both lists are then stored to the same list
('list_of_text_ids_with_all_words'). As the loop runs each list from the value of each key/value pair is compared to
'list_of_text_ids_with_all_words', which will diminish by a text ID every time a list being compared to it does not
contain that particular text ID.

As lists are compared to 'list_of_text_ids_with_all_words', they will surely have text IDs that are not already in
'list_of_text_ids_with_all_words' and those IDs will never be added to 'list_of_text_ids_with_all_words'.