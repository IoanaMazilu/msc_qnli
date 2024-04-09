age_difference_premise = 5
age_difference_hypothesis = 6

# the hypothesis refers to the age difference between Roshan and Raj, also mentioned in the premise
if age_difference_premise > age_difference_hypothesis:
    # check if the age difference in the premise contradicts the age difference in the hypothesis
    label = "contradiction"
elif age_difference_premise < age_difference_hypothesis:
    # check if the age difference in the premise is less than the age difference in the hypothesis
    label = "entailment"
else:
    # if the age difference in the premise and hypothesis are the same, we can infer entailment
    label = "entailment"

print(label)
