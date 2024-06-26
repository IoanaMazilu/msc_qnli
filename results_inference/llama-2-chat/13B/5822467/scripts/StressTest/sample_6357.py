nice_premise = 5
nice_hypothesis = 2

# the hypothesis refers to the number of baseball cards given to John
if nice_hypothesis <= nice_premise:
    # check if the hypothesis value contradicts the number of baseball cards mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of baseball cards
    # any number of baseball cards greater than 'nice_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
