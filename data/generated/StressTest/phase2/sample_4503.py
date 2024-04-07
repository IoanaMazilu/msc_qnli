# Premise: Each week, Harry is paid x dollars per hour for the first 15 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first less than 65 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: entailment

hours_normal_rate_premise = 15
hours_normal_rate_hypothesis = 65

# the hypothesis refers to the number of hours Harry is paid x dollars, mentioned in the premise
if hours_normal_rate_hypothesis > hours_normal_rate_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

