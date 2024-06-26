matched_gloves_premise = 20
matched_gloves_hypothesis = 20

# the hypothesis refers to the number of pairs of gloves Andy has, also mentioned in the premise
if matched_gloves_hypothesis <= matched_gloves_premise:
    # check if the hypothesis value contradicts the number of pairs of gloves reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of gloves
    # any number of pairs of gloves greater than'matched_gloves_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
