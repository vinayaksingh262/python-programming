# Ask a sub name as a input and from the user.print marks of that subject.
# if sub not exist print "invalid"
sub_dict = {"maths": 95, "english": 84, "science": 99, "it": 95, "social science": 86}
sub = input("Enter a subject :")
if sub in sub_dict:
    print(sub_dict[sub])
else:
    print("Invalid")
