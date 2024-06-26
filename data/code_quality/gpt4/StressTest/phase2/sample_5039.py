combinations_premise = 3
combinations_hypothesis = 6
friends_premise = 6
friends_hypothesis = 6

# the hypothesis refers to the number of combinations of passengers and the number of John's friends mentioned in the premise

if friends_hypothesis != friends_premise:
    # check if the number of John's friends in the hypothesis contradicts the number of John's friends reported in the premise
    label = "contradiction"
elif combinations_hypothesis <= combinations_premise:
   # check if the number of combinations in the hypothesis contradicts the number of combinations in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of combinations
    # any number of combinations greater than 'combinations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
