age_difference_premise = 14
age_difference_hypothesis = 84

# the hypothesis talks about the age difference between Frank and John, referenced also in the premise
if age_difference_hypothesis <= age_difference_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives an exact age difference
    # any age difference greater than 'age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
