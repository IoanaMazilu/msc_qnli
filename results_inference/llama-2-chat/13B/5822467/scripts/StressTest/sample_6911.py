roshan_age_premise = 5 * (3 - 1) = 15
raj_age_premise = 3 * (4 - 1) = 12
age_ratio_premise = 3 / 4

roshan_age_hypothesis = 2 * (3 - 1) = 6
raj_age_hypothesis = 3 * (4 - 1) = 12
age_ratio_hypothesis = 3 / 4

# compare the premise and hypothesis values for consistency
if roshan_age_hypothesis > roshan_age_premise:
    # the hypothesis contradicts the premise, as Roshan's age is estimated to be higher than the premise
    label = "contradiction"
elif raj_age_hypothesis!= raj_age_premise:
    # the hypothesis contradicts the premise, as Raj's age is estimated to be different from the premise
    label = "contradiction"
elif age_ratio_hypothesis!= age_ratio_premise:
    # the hypothesis contradicts the premise, as the age ratio is estimated to be different from the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
