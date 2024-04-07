# Premise: Shawn plants a garden less than 65 feet by 24 feet.
# Hypothesis: Shawn plants a garden 25 feet by 24 feet.
# Golden Label: neutral

garden_length_premise = 65
garden_length_hypothesis = 25
garden_width_premise = 24
garden_width_hypothesis = 24

# the hypothesis talks about the size of the garden, referenced also in the premise
if garden_length_hypothesis >= garden_length_premise:
    # check if the hypothesis length contradicts the estimate of less than 'garden_length_premise'
    label = "contradiction"
elif garden_width_hypothesis != garden_width_premise:
    # check if the width of garden in the hypothesis contradicts the width of garden reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the garden size
    # any size less than 'garden_length_premise' and equal to 'garden_width_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

