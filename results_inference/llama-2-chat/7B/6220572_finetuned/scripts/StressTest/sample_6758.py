p_premise = 8
p_hypothesis = 6

if p_hypothesis >= p_premise:
    # check if the number of P in the hypothesis contradicts the number of P in the premise
    label = "contradiction"
else:
    # any number of P less than 'p_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
