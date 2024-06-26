p_premise = 8
p_hypothesis = 6

# the hypothesis refers to the number of P mentioned in the premise
if p_hypothesis <= p_premise:
    # check if the hypothesis value contradicts the estimate of 'p_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of P
    # any number of P greater than 'p_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
