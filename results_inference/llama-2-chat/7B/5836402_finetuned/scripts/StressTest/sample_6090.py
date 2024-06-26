p_premise = 1
p_hypothesis = 3

# the hypothesis refers to the definition of 'Sophie Germain' prime, which is also mentioned in the premise
if p_hypothesis <= p_premise:
    # check if the hypothesis value contradicts the definition of 'Sophie Germain' prime in the premise
    label = "contradiction"
else:
    # the premise gives a definition for 'Sophie Germain' prime, which cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
