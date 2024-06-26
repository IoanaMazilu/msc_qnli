purchased_premise = 20
purchased_hypothesis = 20

# the hypothesis refers to the number of items purchased from Ram by Mohan, mentioned in the premise
if purchased_hypothesis <= purchased_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact number of items purchased
    # any number of items greater than 'purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
