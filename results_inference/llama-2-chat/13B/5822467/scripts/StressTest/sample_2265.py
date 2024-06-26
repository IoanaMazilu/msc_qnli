andy_gloves_premise = 20
andy_gloves_hypothesis = 60

# the hypothesis refers to the number of pairs of matched gloves owned by Andy
if andy_gloves_premise <= andy_gloves_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'andy_gloves_premise'
    label = "contradiction"
else:
    # the premise gives a specific number of pairs of gloves owned by Andy
    # any number of pairs less than 'andy_gloves_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
