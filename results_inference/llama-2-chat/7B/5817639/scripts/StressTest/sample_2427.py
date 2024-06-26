old_age_premise = 5/3
old_age_hypothesis = 7/3

# check if the hypothesis value contradicts the estimate of 'old_age_premise'
if old_age_hypothesis <= old_age_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of roses
    # any number of roses greater than 'roses_vase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
