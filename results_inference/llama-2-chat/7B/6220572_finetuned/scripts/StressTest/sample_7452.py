T_premise = 5/9 * (K-32)
T_hypothesis = 4/9 * (K-32)
T_equal_premise = 105
T_equal_hypothesis = 105

# the hypothesis talks about the T value and the K value referenced in the premise
if T_hypothesis <= T_equal_premise:
    # check if the hypothesis value contradicts the estimate of more than 'T_equal_premise'
    label = "contradiction"
elif T_hypothesis!= T_equal_hypothesis:
    # check if the hypothesis value contradicts the value of T in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the T value
    # any T value greater than 'T_equal_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
