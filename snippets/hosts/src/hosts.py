block_list = []
block_list.append('facebook')
block_list.append('fb')
block_list.append('linkedin')
block_list.append('github')
'''
block_list.append('stackoverflow')
block_list.append('youtube')
block_list.append('gmail')
block_list.append('quora')
'''

block_list_processed = []
for i in block_list:
    i += ".com"
    block_list_processed.append(i)
    block_list_processed.append("www." + i)

block_list_string = "\n\n0.0.0.0"
# print block_string

for i in block_list_processed:
    block_list_string += " " + i

block_list_string += "\n\n"

print block_list_string
