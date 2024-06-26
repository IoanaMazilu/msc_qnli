passengers_combinations_premise = 2
passengers_combinations_hypothesis = 4
friends_number_premise = 6
friends_number_hypothesis = 6

# the hypothesis refers to the number of different combinations of passengers and friends mentioned in the premise
if friends_number_hypothesis!= friends_number_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends reported in the premise
    label = "contradiction"
elif passengers_combinations_hypothesis <= passengers_combinations_premise:
    # check if the number of passengers combinations in the hypothesis contradicts the estimate of more than 'passengers_combinations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers combinations
    # any number of combinations greater than 'passengers_combinations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)