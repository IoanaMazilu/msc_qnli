portion_premise = 7/12
portion_hypothesis = 7/12

# the hypothesis refers to the same portion of money Anup was asked to find in the premise
if portion_hypothesis <= portion_premise:
    # check if the hypothesis value contradicts the estimate of more than 'portion_hypothesis'
    label = "contradiction"
else:
    # the premise gives only an estimate for the portion of money
    # any portion greater than 'portion_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
