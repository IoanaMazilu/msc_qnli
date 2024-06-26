T_premise = 5/9 * (K-32)
T_hypothesis = 2/9 * (K-32)

# the hypothesis talks about the T equation in the premise
if T_hypothesis <= T_premise:
    # check if the hypothesis value contradicts the estimate of more than 'T_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the T equation
    # any T equation greater than 'T_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
