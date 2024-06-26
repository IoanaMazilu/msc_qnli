p_premise = 4
p_hypothesis = 8

# the hypothesis talks about the amount of P Tom goes after, referenced also in the premise
if p_hypothesis <= p_premise:
    # check if the hypothesis value contradicts the estimate of more than 'p_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of P
    # any amount of P greater than 'p_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
