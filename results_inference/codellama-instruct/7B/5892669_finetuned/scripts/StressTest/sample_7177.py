total_premise = 3800
total_hypothesis = 4800

# the hypothesis refers to the total number mentioned in the premise
if total_hypothesis <= total_premise:
    # check if the total number in the hypothesis contradicts the estimate of more than 'total_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number
    # any total number greater than 'total_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
