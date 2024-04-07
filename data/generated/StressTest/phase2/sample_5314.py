# Premise: Sandy is younger than Molly by less than 30 years.
# Hypothesis: Sandy is younger than Molly by 20 years.
# Golden Label: neutral

age_diff_premise = 30
age_diff_hypothesis = 20

# the hypothesis talks about the age difference between Sandy and Molly, referenced also in the premise
if age_diff_hypothesis >= age_diff_premise:
    # check if the hypothesis value contradicts the estimate of less than 'age_diff_premise'
    label = "contradiction"
elif age_diff_hypothesis < age_diff_premise:
    # the age difference in hypothesis is less than the premise's age difference
    # thus, the hypothesis does not contradict the premise, but it cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)

