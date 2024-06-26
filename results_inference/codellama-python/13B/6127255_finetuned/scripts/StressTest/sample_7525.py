passengers_premise = 2
passengers_hypothesis = 4
friends_premise = 6
friends_hypothesis = 6

# the hypothesis refers to the number of passengers and friends mentioned in the premise
if passengers_hypothesis <= passengers_premise:
    # check if the number of 'passengers_hypothesis' contradicts the number of passengers in the premise
    label = "contradiction"
elif friends_hypothesis!= friends_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers
    # any number of passengers greater than 'passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
