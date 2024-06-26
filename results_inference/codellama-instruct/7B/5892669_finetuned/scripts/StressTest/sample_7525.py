passengers_combinations_premise = 2
passengers_combinations_hypothesis = 4
friends_premise = 6
friends_hypothesis = 6

# the hypothesis refers to the number of passenger combinations and friends mentioned in the premise
if passengers_combinations_hypothesis <= passengers_combinations_premise:
    # check if the number of passenger combinations in the hypothesis contradicts the estimate of more than 'passengers_combinations_premise'
    label = "contradiction"
elif friends_hypothesis!= friends_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passenger combinations
    # any number of passenger combinations greater than 'passengers_combinations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
