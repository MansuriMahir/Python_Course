#get 5 age, name , bloodgroup, height from user
age = input("enter your age:")
name = input("enter your name:")
bloodgroup = input("enter your bloodgroup:")
height = input("enter your height:")
# print(f'\n your age is {age}, \n your name is {name}, \n your bloodgroup is {bloodgroup}, \n your height is {height}')
print('your age is ' + age + ' ' + 'your name is' + name + ' ' + 'your bloodgroup is' + bloodgroup + ' ' + 'your height is' + height)


#print 3 paragraph  from that get ever 12th words 
abc = """
hello world
how are you 
i am fine 
"""
print(abc)

# print every 3 words frm the string 
words = "Google is a multinational technology corporation, primarily known for its powerful search engine Google Search, and a wide range of other products and services. Google's 'https://about.google/products/' 'website offers various tools including maps, email (Gmail), cloud storage (Google Drive), a document suite, and an operating system (Android). Google also has a significant presence in advertising, AI, and hardware, with the goal of organizing the world's information and making it universally accessible and useful. "
#        012345678901234567891010
print(words[9:24]) 
print(words[::-1])
