passengers_combination_premise = 2
passengers_combination_hypothesis = 4
friends_number_premise = 6
friends_number_hypothesis = 6

# the hypothesis refers to the number of passengers combinations and friends number mentioned in the premise
if passengers_combination_hypothesis <= passengers_combination_premise:
    # check if the hypothesis value contradicts the estimate of more than 'passengers_combination_premise'
    label = "contradiction"
elif friends_number_hypothesis!= friends_number_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers combinations
    # any number of passengers combinations greater than 'passengers_combination_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
