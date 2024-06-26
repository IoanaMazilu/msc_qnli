# defining the variables for the premise and hypothesis
p_premise = 1
p_hypothesis = 4

# the hypothesis refers to the definition of a Sophie Germain prime, also mentioned in the premise
if p_premise >= p_hypothesis:
    # check if the premise value contradicts the definition of a Sophie Germain prime in the hypothesis
    label = "contradiction"
elif p_premise < p_hypothesis:
    # if the premise value is less than the hypothesis value, it can be explicitly entailed from the hypothesis
    label = "entailment"

print(label)
