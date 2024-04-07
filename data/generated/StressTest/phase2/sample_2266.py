# Premise: Andy has less than 60 pairs of matched gloves.
# Hypothesis: Andy has 20 pairs of matched gloves.
# Golden Label: neutral

gloves_premise = 60
gloves_hypothesis = 20

# the hypothesis refers to the number of matched gloves Andy has, mentioned also in the premise
if gloves_hypothesis >= gloves_premise:
    # check if the number of gloves in the hypothesis contradicts the premise of less than 'gloves_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gloves
    # any number of gloves less than 'gloves_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

