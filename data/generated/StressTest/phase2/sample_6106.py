# Premise: Jane is currently less than 82 years old, and she stopped baby-sitting 12 years ago.
# Hypothesis: Jane is currently 32 years old, and she stopped baby-sitting 12 years ago.
# Golden Label: neutral

jane_age_premise = 82
jane_age_hypothesis = 32
years_babysitting_premise = 12
years_babysitting_hypothesis = 12

# the hypothesis refers to Jane's age and the years since she stopped babysitting, both also mentioned in the premise
if jane_age_hypothesis >= jane_age_premise:
    # check if the age in the hypothesis contradicts the estimate of less than 'jane_age_premise'
    label = "contradiction"
elif years_babysitting_premise != years_babysitting_hypothesis:
    # check if the number of years since Jane stopped babysitting in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
elif jane_age_hypothesis < jane_age_premise and years_babysitting_premise == years_babysitting_hypothesis:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones nor can be entailed, we infer neutrality
    label = "neutral"

print(label)

