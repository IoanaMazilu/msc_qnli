p_premise = 2
p_hypothesis = 4

# the hypothesis refers to the same concept of "Sophie Germain" prime as the premise
if p_hypothesis <= p_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif p_hypothesis > p_premise:
    # if the hypothesis value is greater than the premise value, it is consistent with the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is consistent with the premise
    label = "neutral"

print(label)
