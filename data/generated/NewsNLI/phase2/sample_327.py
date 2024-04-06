# Premise: Sweety High caters to girls between 8 and 16 and wraps'' social gaming mechanics around an arts platform,'' CEO and co-founder Frank Simonetti said.
# Hypothesis: Sweety High is a social gaming site for tween and teen girls between ages 8 and 16.
# Golden Label: entailment

lower_age_limit_premise = 8
upper_age_limit_premise = 16
lower_age_limit_hypothesis = 8
upper_age_limit_hypothesis = 16

# the hypothesis mentions the age range for users of Sweety High, which is also mentioned in the premise
if lower_age_limit_hypothesis != lower_age_limit_premise:
    # check if the lower age limit from the hypothesis contradicts the lower age limit in the premise
    label = "contradiction"
elif upper_age_limit_hypothesis != upper_age_limit_premise:
    # check if the upper age limit from the hypothesis contradicts the upper age limit in the premise
    label = "contradiction"
else:
    # if the hypothesis age range does not contradict the premise age range, we can infer entailment
    label = "entailment"

print(label)

