# Premise: Mary is less than 42 years younger than Albert.
# Hypothesis: Mary is 22 years younger than Albert.
# Golden Label: neutral

age_difference_premise = 42
age_difference_hypothesis = 22

# the hypothesis refers to the age difference between Mary and Albert mentioned in the premise
if age_difference_hypothesis > age_difference_premise:
    # check if the age difference in the hypothesis contradicts the estimate of less than 'age_difference_premise'
    label = "contradiction"
elif age_difference_hypothesis < age_difference_premise:
    # any age difference less than 'age_difference_premise' is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"
else:
    # if the age difference in the hypothesis equals 'age_difference_premise', it is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

