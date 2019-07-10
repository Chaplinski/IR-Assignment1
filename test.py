import os

# create dictionary

text_files = os.listdir("collection2/")

this_dict = {}
this_list = []

this_dict.update({'scooby': [['Text-001.txt', [1, 4, 9]], ['Text-002.txt', [2, 5, 139, 4]]]})
this_list = ['Text-003.txt', [1, 4, 9]]
this_dict['scooby'].append(this_list)

new_words = ['plethora', 'Jack', 'scooby']
text = 'Text-009.txt'
integer = 522
# for every word in a text
for potential_new_word in new_words:
    # check if the word already exists in the dictionary
    if potential_new_word in this_dict:
        # if word does exist then access its value array
        # print(potential_new_word)
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
        this_dict.update({potential_new_word: new_list})

print(this_dict)
