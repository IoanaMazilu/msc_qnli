# Premise: 12 year old Manick is three times as old as his brother Rahul.
# Hypothesis: less than 22 year old Manick is three times as old as his brother Rahul.
# Golden Label: entailment

manick_age_premise = 12
rahul_age_premise = manick_age_premise / 3
manick_age_hypothesis = 22
rahul_age_hypothesis = manick_age_hypothesis / 3

# the hypothesis refers to the age of Manick and Rahul mentioned in the premise
if manick_age_hypothesis <= manick_age_premise:
    # check if the estimate of 'manick_age_hypothesis' contradicts the age of Manick in the premise
    label = "contradiction"
elif rahul_age_hypothesis != rahul_age_premise:
    # check if the age of Rahul in the hypothesis contradicts the age of Rahul in the premise
    label = "contradiction"
else:
    # the premise gives only the exact age of Manick and Rahul, 
    # any age of Manick less than 'manick_age_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

