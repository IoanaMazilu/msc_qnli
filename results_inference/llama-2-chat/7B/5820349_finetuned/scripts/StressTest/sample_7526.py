passengers_combinations_premise = 4
passengers_combinations_hypothesis = 4
friends_number = 6

# the hypothesis refers to the number of passengers combinations mentioned in the premise
if passengers_combinations_hypothesis <= passengers_combinations_premise:
    # check if the hypothesis value contradicts the number of passengers combinations in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
