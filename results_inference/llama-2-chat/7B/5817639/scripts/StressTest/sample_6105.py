jane_age_premise = 32
jane_age_hypothesis = 82

# the hypothesis talks about Jane's age, which is also mentioned in the premise
if jane_age_hypothesis <= jane_age_premise:
    # check if the hypothesis value contradicts the estimate of Jane's age in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for Jane's age, which cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
