# Premise: Arun makes a popular brand of ice cream in a rectangular shaped bar 6 cm long, 5 cm wide and 2 cm thick.
# Hypothesis: Arun makes a popular brand of ice cream in a rectangular shaped bar more than 1 cm long, 5 cm wide and 2 cm thick.
# Golden Label: entailment

length_premise = 6
width_premise = 5
thickness_premise = 2

length_hypothesis = 1
width_hypothesis = 5
thickness_hypothesis = 2

# the hypothesis refers to the dimensions of the ice cream bar mentioned in the premise
if length_premise <= length_hypothesis:
    # check if the estimate of 'length_hypothesis' contradicts the length in the premise
    label = "contradiction"
elif width_hypothesis != width_premise or thickness_hypothesis != thickness_premise:
    # check if the width and thickness in the hypothesis contradict the width and thickness reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

