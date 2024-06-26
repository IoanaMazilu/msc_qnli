age_difference_premise = 6
age_difference_hypothesis = 7
ratio_premise = 7/9
ratio_hypothesis = 7/9

# the hypothesis talks about the age difference and ratio between Kiran and Bineesh, referenced also in the premise
if age_difference_hypothesis <= age_difference_premise:
    # check if the hypothesis value contradicts the estimate of more than 'age_difference_premise'
    label = "contradiction"
elif ratio_hypothesis!= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age difference
    # any age difference greater than 'age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
