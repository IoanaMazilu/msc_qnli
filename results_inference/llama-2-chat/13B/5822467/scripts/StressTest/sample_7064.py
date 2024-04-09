stv_premise = (ST, TV, SV) = (26, 26, 20)
stv_hypothesis = (ST, TV, SV) = (less than 26, less than 26, 20)

# the hypothesis refers to the sides of the triangle STV
if stv_premise[0] <= stv_hypothesis[0] and stv_premise[1] <= stv_hypothesis[1] and stv_premise[2] == stv_hypothesis[2]:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
elif stv_hypothesis[0] > stv_premise[0] or stv_hypothesis[1] > stv_premise[1] or stv_hypothesis[2]!= stv_premise[2]:
    # the hypothesis values contradict the premise ones, so we can infer contradiction
    label = "contradiction"
else:
    # the premise gives a specific value for the sides of the triangle, and the hypothesis does not contradict it
    # any value of the sides of the triangle consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
