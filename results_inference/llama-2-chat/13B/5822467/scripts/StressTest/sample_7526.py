friend_count_premise = 6
combination_size_premise = 4

# define variables for the hypothesis
friend_count_hypothesis = 7
combination_size_hypothesis = 5

# check if the hypothesis value contradicts the premise estimate
if combination_size_hypothesis > combination_size_premise:
    label = "contradiction"
elif friend_count_hypothesis > friend_count_premise:
    label = "entailment"
else:
    # the hypothesis values do not contradict the premise values, so we have neutrality
    label = "neutral"

print(label)
