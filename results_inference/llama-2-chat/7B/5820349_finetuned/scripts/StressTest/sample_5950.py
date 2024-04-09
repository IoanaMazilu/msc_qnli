t_premise = 20
t_hypothesis = 20

# the hypothesis refers to the value of T mentioned in the premise
if t_hypothesis!= t_premise:
    # check if the value of T in the hypothesis contradicts the value of T reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the value of T
    # any value of T equal to 't_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
