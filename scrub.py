# scrub_lyrics(text)
# Description:  takes a text file of lyrics and scrubs 
# 			  file from other text from the website, new lines,
# 			  and punctuation (besides apostrophes)
# param      :  the name of a text file that has lyrics from AZLyrics
# return     :  scrubbed lyrics

def scrub_lyrics(text):
	big_ass_text = open(text)
	lines = big_ass_text.readlines()
	ret = []										# list of scrubbed lines

	for i in range(8, len(lines)):					# always 8 lines before actual lyrics
		if lines[i] == "Submit Corrections\n":		# loop control flow
			break									# pages all end this way
		if lines[i] == "\n":						# don't add blank lines
			continue

##### NOTE FROM HERE ON IS A METHOD IN RHYME DETECT, SO WHEN WE PUT THEM TOGETHER CHANGE THIS TO METHOD ########

		line = lines[i].split()						# this is a line we want to process
		temp_line = []								# current scrubbed line
		for j in line:								# go word by word
			if j.isalpha():							# no punctuation to remove in this word in the line
				temp_line.append(j)					# add normaly
			else:									# there is punctuation to remove
				temp_word = []
				for k in j:						# go letter by letter
					if k.isalpha() or k == "'":					# this is not a punctuation character
						temp_word.append(k)			# add to the currnet scrubbed word
				temp_line.append("".join(temp_word))
		ret.append(" ".join(temp_line))				# add to list of scrubbed lines
	print ret

scrub_lyrics("rap_god.txt")