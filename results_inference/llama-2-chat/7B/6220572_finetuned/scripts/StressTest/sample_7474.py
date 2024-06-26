p_premise = 4
p_hypothesis = 2

# the hypothesis refers to the number of p mentioned in the premise
if p_hypothesis <= p_premise:
    # check if the hypothesis value contradicts the estimate of 'p_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of p
    # any number of p greater than 'p_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
