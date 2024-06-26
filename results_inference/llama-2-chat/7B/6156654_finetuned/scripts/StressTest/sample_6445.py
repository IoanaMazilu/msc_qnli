frank_age_premise = 84
john_age_premise = 84
frank_age_hypothesis = 14

# the hypothesis talks about the age of Frank and John, which is also mentioned in the premise
if frank_age_hypothesis <= frank_age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif john_age_premise - frank_age_premise > frank_age_hypothesis:
    # check if the difference between John's age and Frank's age in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
