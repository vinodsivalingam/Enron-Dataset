# Creates a word map with the corresponding position for each file
def file_index(fileslist):
	index_file = {}
	for index, word in enumerate(fileslist):
		if word in index_file.keys():
			index_file[word].append(index)
		else:
			index_file[word] = [index]
	return index_file
 
 
# Each file is iterated and using the above mapping, the function will
# return word mapping with corresponding position for each file
def word_indices(fileslist):
	result = {}
	for eachfile in fileslist.keys():
		result[eachfile] = index_one_file(fileslist[eachfile])
	return result
  
  def finalIndex(regx):
	final_index = {}
	for file in regx.keys():
		for eachvalue in regx[file].keys():
			if eachvalue in final_index.keys():
				if file in final_index[eachvalue].keys():					               
          final_index[eachvalue][file].extend(regx[file][eachvalue][:])
				else:
					final_index[eachvalue][file] = regx[file][eachvalue]                        
			else:
				final_index[eachvalue] = {file: regx[file][eachvalue]}
	return final_index
