friends_premise = 6
different_combinations_premise = 2
different_combinations_hypothesis = 4

# the hypothesis refers to the number of different combinations of passengers mentioned in the premise
if different_combinations_hypothesis <= different_combinations_premise:
    # check if the hypothesis value contradicts the estimate of more than 'different_combinations_premise'
    label = "contradiction"
elif different_combinations_hypothesis > different_combinations_premise:
    # if the hypothesis value is greater than the premise, it is entailed
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise, it is neutral
    label = "neutral"

print(label)
