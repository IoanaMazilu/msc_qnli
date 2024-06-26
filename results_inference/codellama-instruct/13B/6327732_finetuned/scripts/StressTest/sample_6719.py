# define variables for the number of jelly beans each child has
aaron_beans = 5
bianca_beans = 7
callie_beans = 8
dante_beans = 13

# check if the number of jelly beans each child has contradicts the premise
if aaron_beans!= 2:
    label = "contradiction"
elif bianca_beans!= 7:
    label = "contradiction"
elif callie_beans!= 8:
    label = "contradiction"
elif dante_beans!= 13:
    label = "contradiction"
else:
    label = "entailment"

print(label)
