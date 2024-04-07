# Premise: Jane is currently 34 years old, and she stopped baby-sitting 12 years ago.
# Hypothesis: Jane is currently less than 54 years old, and she stopped baby-sitting 12 years ago.
# Golden Label: entailment

jane_age_premise = 34
jane_age_hypothesis = 54
babysitting_stop_years_premise = 12
babysitting_stop_years_hypothesis = 12

# the hypothesis refers to Jane's current age and the years since she stopped baby-sitting, mentioned also in the premise
if jane_age_premise >= jane_age_hypothesis:
    # check if 'jane_age_premise' contradicts the hypothesis that Jane is less than 54 years old
    label = "contradiction"
elif babysitting_stop_years_premise != babysitting_stop_years_hypothesis:
    # check if the years since Jane stopped baby-sitting in the premise contradict the same value in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

