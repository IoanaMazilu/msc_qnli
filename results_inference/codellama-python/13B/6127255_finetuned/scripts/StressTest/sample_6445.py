frank_age_diff_premise = 84
frank_age_diff_hypothesis = 14

# the hypothesis talks about the age difference between Frank and John, which is also referenced in the premise
if frank_age_diff_hypothesis > frank_age_diff_premise:
    # check if the hypothesis value contradicts the estimate of less than 'frank_age_diff_premise'
    label = "contradiction"
elif frank_age_diff_hypothesis < frank_age_diff_premise:
    # the premise gives only an estimate for the age difference
    # any age difference less than 'frank_age_diff_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise's estimate, we can infer entailment
    label = "entailment"

print(label)
