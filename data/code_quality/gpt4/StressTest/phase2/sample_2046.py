age_difference_premise = 18
age_difference_hypothesis = 78

# the hypothesis refers to the age difference between Sandy and Molly mentioned in the premise
if age_difference_premise >= age_difference_hypothesis:
    # check if the premise contradicts the 'age_difference_hypothesis'
    label = "contradiction"
elif age_difference_premise != age_difference_hypothesis:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
