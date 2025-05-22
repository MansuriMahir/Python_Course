is_magician = True
is_expert = True 

# Check if magicin and expert: you are a master magician 
if is_expert and is_magician:
    print("You are a master magician!") 

#Check if magician but not expert:"at least you're a gretting there"
elif is_magician and not is_expert:
    print("At least you're a gentle magician!")

#IF you are not a magician: YOU need magic power "
elif not is_magician:
    print("you need magic power!")