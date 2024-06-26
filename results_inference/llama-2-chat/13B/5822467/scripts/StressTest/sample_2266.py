andy_gloves_premise = 60
andy_gloves_hypothesis = 20

# the hypothesis refers to the number of pairs of matched gloves
if andy_gloves_hypothesis <= andy_gloves_premise:
    # check if the hypothesis value contradicts the estimate of 'andy_gloves_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of matched gloves
    # any number of pairs of matched gloves less than or equal to 'andy_gloves_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
