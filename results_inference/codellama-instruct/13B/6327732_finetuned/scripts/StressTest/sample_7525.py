num_friends_premise = 6
num_friends_hypothesis = 4

# the hypothesis refers to the number of passengers in a combination, which is not explicitly mentioned in the premise
if num_friends_hypothesis <= num_friends_premise:
    # check if the hypothesis value contradicts the number of friends mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of combinations
    # any number of combinations greater than the estimate in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
