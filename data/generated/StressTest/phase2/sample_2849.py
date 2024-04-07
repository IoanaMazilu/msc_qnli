# Premise: Andy has 20 pairs of matched gloves.
# Hypothesis: Andy has less than 20 pairs of matched gloves.
# Golden Label: contradiction

gloves_premise = 20
gloves_hypothesis = 20

# the hypothesis talks about the number of gloves Andy has, referenced also in the premise
if gloves_hypothesis >= gloves_premise:
    # check if the hypothesis value contradicts the premise of having less than 'gloves_premise'
    label = "contradiction"
else:
    # if the number of gloves in the hypothesis is less than 'gloves_premise', it can be entailed from the premise
    label = "entailment"

print(label)

