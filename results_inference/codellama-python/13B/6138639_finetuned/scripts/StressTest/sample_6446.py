age_difference_premise = 14
age_difference_hypothesis = 54

# the hypothesis talks about the age difference between Frank and John, referenced also in the premise
if age_difference_hypothesis!= age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
