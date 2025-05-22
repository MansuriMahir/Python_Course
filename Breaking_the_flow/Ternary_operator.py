#Ternary operator
#
is_friend = False
her_friend = True
can_message = "Message Allowed" if is_friend else "Message Not Allowed" if her_friend else "No Friend Available"

print(can_message)