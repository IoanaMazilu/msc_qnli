purchased_each_premise = 20
purchased_each_hypothesis = 20

# the hypothesis refers to the number of purchased items, which is also mentioned in the premise
if purchased_each_hypothesis <= purchased_each_premise:
    # check if the estimate of 'purchased_each_hypothesis' contradicts the number of purchased items in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of purchased items
    # any number of purchased items greater than 'purchased_each_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
