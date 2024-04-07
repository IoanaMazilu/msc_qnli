# Premise: less than 22 year old Manick is three times as old as his brother Rahul.
# Hypothesis: 12 year old Manick is three times as old as his brother Rahul.
# Golden Label: neutral

manick_age_premise = 22
manick_age_hypothesis = 12
rahul_age_hypothesis = manick_age_hypothesis / 3
rahul_age_premise = manick_age_premise / 3

# the hypothesis talks about the age of Manick and Rahul, referenced also in the premise
if manick_age_hypothesis >= manick_age_premise:
    # check if the hypothesis value contradicts the estimate of less than 'manick_age_premise'
    label = "contradiction"
elif rahul_age_hypothesis != rahul_age_premise:
    # check if the age of Rahul in the hypothesis contradicts the age of Rahul calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

