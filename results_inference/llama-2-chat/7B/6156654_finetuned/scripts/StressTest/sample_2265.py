andy_gloves_premise = 20
andy_gloves_hypothesis = 60

# the hypothesis refers to the number of pairs of gloves Andy has, which is also mentioned in the premise
if andy_gloves_hypothesis <= andy_gloves_premise:
    # check if the hypothesis value contradicts the premise value
    label = "entailment"
elif andy_gloves_hypothesis > andy_gloves_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it is neutral
    label = "neutral"

print(label)
