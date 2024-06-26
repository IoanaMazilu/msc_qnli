arun_age_premise = 4
deepak_age_premise = 3
arun_age_hypothesis = 1
deepak_age_hypothesis = 3

# the hypothesis refers to the ratio of their ages, which is also mentioned in the premise
if arun_age_hypothesis == deepak_age_hypothesis:
    # the hypothesis and premise have the same ratio, so there is no contradiction or entailment
    label = "neutral"
elif arun_age_hypothesis > deepak_age_hypothesis:
    # the hypothesis states a different ratio than the premise, so there is a contradiction
    label = "contradiction"
else:
    # the hypothesis states a ratio that is consistent with the premise, so there is entailment
    label = "entailment"

print(label)
