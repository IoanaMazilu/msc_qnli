jane_age_premise = 82
jane_age_hypothesis = 32

# the hypothesis talks about the current age of Jane, which is also mentioned in the premise
if jane_age_hypothesis <= jane_age_premise:
    # check if the hypothesis value contradicts the estimate of Jane's current age in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for Jane's current age, and the hypothesis value is consistent with that estimate
    label = "entailment"

print(label)
