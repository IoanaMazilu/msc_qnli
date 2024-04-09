p_premise = 2
p_hypothesis = 3

# the hypothesis refers to the condition of a Sophie Germain prime mentioned in the premise
if p_hypothesis <= p_premise:
    # check if the hypothesis value contradicts the condition of 'less than p_premise'
    label = "contradiction"
else:
    # the premise gives the exact condition for a Sophie Germain prime
    # any condition less than 'p_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
