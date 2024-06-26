months_premise = 3
months_hypothesis = 4

# the hypothesis refers to the duration of months mentioned in the premise
if months_hypothesis <= months_premise:
    # check if the number of months in the hypothesis contradicts the estimate of more than 'months_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of months
    # any number of months greater than 'months_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
