# Premise: Jane is currently less than 54 years old, and she stopped baby-sitting 10 years ago.
# Hypothesis: Jane is currently 34 years old, and she stopped baby-sitting 10 years ago.
# Golden Label: neutral

jane_age_premise = 54
jane_age_hypothesis = 34
babysitting_stop_premise = 10
babysitting_stop_hypothesis = 10

# the hypothesis refers to Jane's age and the number of years since she stopped babysitting, both mentioned in the premise
if jane_age_hypothesis >= jane_age_premise:
    # check if the hypothesis age contradicts the premise's upper age limit for Jane
    label = "contradiction"
elif babysitting_stop_hypothesis != babysitting_stop_premise:
    # check if the years since Jane stopped babysitting in the hypothesis contradicts the years reported in the premise
    label = "contradiction"
else:
    # the age of Jane in the hypothesis is less than the upper age limit in the premise and the years since she stopped babysitting is the same
    # this means the hypothesis does not contradict the premise, but we cannot fully and explicitly infer Jane's exact age from the premise
    label = "neutral"

print(label)

