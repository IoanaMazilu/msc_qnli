# define variables for the numerical entities in the premise
scores_less_than_7 = 1
scores_2 = 1
scores_3 = 1
scores_4 = 1

# define variables for the numerical entities in the hypothesis
scores_1 = 1
scores_2 = 1
scores_3 = 1
scores_4 = 1

# check if the hypothesis values contradict the premise values
if scores_1 <= scores_less_than_7:
    label = "contradiction"
elif scores_2 <= scores_2:
    label = "contradiction"
elif scores_3 <= scores_3:
    label = "contradiction"
elif scores_4 <= scores_4:
    label = "contradiction"
else:
    label = "neutral"

print(label)
