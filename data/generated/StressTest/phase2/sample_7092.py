# Premise: Ratio between Rahul and Deepak is 5:2, After 6 Years Rahul age will be 26 years.
# Hypothesis: Ratio between Rahul and Deepak is less than 8:2, After 6 Years Rahul age will be 26 years.
# Golden Label: entailment

ratio_premise = 5/2
ratio_hypothesis = 8/2
rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# the hypothesis refers to the age ratio and future age of Rahul, both mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

