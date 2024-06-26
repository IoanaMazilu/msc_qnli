tip_premise = 15
tip_hypothesis = 25

# the hypothesis refers to the tip percentage paid by John and Jane, mentioned also in the premise
if tip_hypothesis <= tip_premise:
    # check if the hypothesis value contradicts the estimate of 'tip_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the tip percentage paid by John and Jane
    # any tip percentage greater than 'tip_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
