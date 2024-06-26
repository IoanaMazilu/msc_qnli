purchased_each_premise = 20
purchased_each_hypothesis = 20

# the hypothesis refers to the number of items purchased, which is also mentioned in the premise
if purchased_each_hypothesis <= purchased_each_premise:
    # check if the hypothesis value contradicts the estimate of more than 'purchased_each_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of items purchased
    # any number of items greater than 'purchased_each_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
