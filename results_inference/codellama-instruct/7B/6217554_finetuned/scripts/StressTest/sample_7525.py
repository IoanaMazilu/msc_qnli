passengers_combinations_premise = 2
passengers_combinations_hypothesis = 4

if passengers_combinations_hypothesis <= passengers_combinations_premise:
    # check if the number of passengers in the hypothesis contradicts the estimate of more than 'passengers_combinations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers
    # any number of passengers greater than 'passengers_combinations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
