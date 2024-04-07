# Premise: Arun makes a popular brand of ice cream in a rectangular shaped bar 6 cm long, 5 cm wide and 2 cm thick.
# Hypothesis: Arun makes a popular brand of ice cream in a rectangular shaped bar less than 6 cm long, 5 cm wide and 2 cm thick.
# Golden Label: contradiction

length_premise = 6
length_hypothesis = 6
width_premise = 5
width_hypothesis = 5
thickness_premise = 2
thickness_hypothesis = 2

# The hypothesis mentions the dimensions of the ice cream bar, which are also mentioned in the premise
if length_hypothesis >= length_premise:
    # Check if the length in the hypothesis contradicts the length in the premise
    label = "contradiction"
elif width_hypothesis != width_premise or thickness_hypothesis != thickness_premise:
    # Check if the width or thickness in the hypothesis contradicts the width or thickness in the premise
    label = "contradiction"
else:
    # If the dimensions in the hypothesis do not contradict the dimensions in the premise, we can infer entailment
    label = "entailment"

print(label)

