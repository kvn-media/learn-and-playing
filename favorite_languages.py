favorite_languages = {
	'jen': ['python', 'ruby'], 
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'hashkell'],
}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")

# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
# 	print(language.title())

# for name in sorted(favorite_languages.keys()):
# 	print(f"{name.title()}, thank you for taking the poll.")

# if 'erin' not in favorite_languages.keys():
# 	print("Erin, please take our poll!")


# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
# 	print(name.title())

# 	if name in friends:
# 		language = favorite_languages[name].title()
# 		print(f"Hi {name.title()}, \nI see you love {language}!")


# for name in favorite_languages.keys():
# 	print(name.title())

# for name, language in favorite_languages.items():
# 	print(f"{name.title()}'s favorite language is {language.title()}.")

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite_languages is {language}.")