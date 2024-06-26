p_premise = 2
p_hypothesis = 8

# the hypothesis refers to the number of P Ana goes before, also mentioned in the premise
if p_hypothesis <= p_premise:
    # check if the estimate of 'p_hypothesis' contradicts the number of P in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of P
    # any number of P greater than 'p_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
