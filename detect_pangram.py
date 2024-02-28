def is_pangram(s):
	# Convert the string to lowercase for case-insensitivity
	s_lower = s.lower()

	# Filter out non-alphabetic characters
	s_alpha = ''.join(char for char in s_lower if char.isalpha())

	# Iterate over each lowercase letter from 'a' to 'z'
	for letter in 'abcdefghijklmnopqrstuvwxyz':
		# Check if the letter is not in the filtered string
		if letter not in s_alpha:
			return False

	# If the loop completes without returning False, the string is a pangram
	return True


print(is_pangram('The quick brown fox jumps over the lazy dog'))
