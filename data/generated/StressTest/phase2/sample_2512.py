# Premise: Arun makes a popular brand of ice cream in a rectangular shaped bar more than 1 cm long, 5 cm wide and 2 cm thick.
# Hypothesis: Arun makes a popular brand of ice cream in a rectangular shaped bar 6 cm long, 5 cm wide and 2 cm thick.
# Golden Label: neutral

length_premise = 1
width_premise = 5
thickness_premise = 2

length_hypothesis = 6
width_hypothesis = 5
thickness_hypothesis = 2

# the hypothesis talks about the dimensions of an ice cream bar, which are also referenced in the premise
if length_hypothesis <= length_premise or width_hypothesis != width_premise or thickness_hypothesis != thickness_premise:
    # check if the dimensions given in the hypothesis contradict the dimensions or estimates given in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the length of the ice cream bar
    # any length greater than 'length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

