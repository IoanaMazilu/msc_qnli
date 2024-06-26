T_premise = 20
T_hypothesis = 20

# the hypothesis refers to the value of T mentioned in the premise
if T_premise!= T_hypothesis:
    # check if the value of 'T_hypothesis' contradicts the value of T in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the value of T
    # any value of T equal to 'T_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
