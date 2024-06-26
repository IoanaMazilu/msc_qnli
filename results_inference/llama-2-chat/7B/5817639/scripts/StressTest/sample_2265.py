matched_gloves_premise = 20
matched_gloves_hypothesis = 60

# the hypothesis talks about the number of pairs of matched gloves, which is also referred to in the premise
if matched_gloves_hypothesis <= matched_gloves_premise:
    # check if the hypothesis value contradicts the estimate of more than'matched_gloves_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of matched gloves
    # any number of pairs of matched gloves greater than'matched_gloves_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
