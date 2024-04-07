# Premise: Ratio between Rahul and Deepak is less than 6:3, After 6 Years Rahul age will be 30 years.
# Hypothesis: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 30 years.
# Golden Label: neutral

ratio_premise = 6 / 3
ratio_hypothesis = 4 / 3
rahul_age_future_premise = 30
rahul_age_future_hypothesis = 30

# the hypothesis refers to the ratio between Rahul and Deepak and Rahul's future age, both mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if Rahul's future age in the hypothesis contradicts Rahul's future age in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

