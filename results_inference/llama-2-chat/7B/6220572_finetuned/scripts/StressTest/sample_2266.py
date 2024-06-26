matched_gloves_premise = 60
matched_gloves_hypothesis = 20

# the hypothesis refers to the number of pairs of matched gloves mentioned in the premise
if matched_gloves_hypothesis <= matched_gloves_premise:
    # check if the hypothesis value contradicts the estimate of more than'matched_gloves_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gloves
    # any number of gloves greater than'matched_gloves_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
