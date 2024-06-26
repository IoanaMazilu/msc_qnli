# define variables for the number of young men killed and the number of children killed
young_men_killed = 23
children_killed = 4

# check if the number of young men killed contradicts the number of children killed
if young_men_killed < children_killed:
    label = "contradiction"
else:
    label = "neutral"

print(label)
