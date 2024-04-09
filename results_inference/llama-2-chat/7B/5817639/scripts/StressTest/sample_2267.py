matched_gloves_premise = 20
matched_gloves_hypothesis = float(20) # assume hypothesis is a float value

# check if the hypothesis value contradicts the estimate of'matched_gloves_premise'
if matched_gloves_hypothesis > matched_gloves_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of matched gloves
    # any number of matched gloves greater than'matched_gloves_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
