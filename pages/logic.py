# sentence = "can IT count this test when this test has many words"


# sentence = sentence.replace(',', '').lower().split()

# dict = {}



# # keys = exists
# for word in sentence:
#     if word in dict.keys():
#         dict[word] += 1
#     else:
#         dict[word] = 1
        
# print(dict)

sentence = "can IT IT count this test when this test has many words leaked"
words = sentence.lower().split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_count:
    if count >= 2:
        print(f"{word}: {count} count")

























# key = argument of sorted and x{1} is based on context
# print("Most common words:")
# for word, count in sorted_count:
#     print(f"{word}: {count}")

# print("Words occurring more than twice:")
# for word, count in word_count.items():
#     if count > 2:
#         print(f"{word} over 2")
    

    
    # do you chosen words and do if has unix etc x3 then put into category 
    # save to db to get it to the internet 
