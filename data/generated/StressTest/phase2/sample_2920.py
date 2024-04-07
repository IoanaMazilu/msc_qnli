# Premise: Ratio between Rahul and Deepak is less than 8:2, After 6 Years Rahul age will be 22 years.
# Hypothesis: Ratio between Rahul and Deepak is 4:2, After 6 Years Rahul age will be 22 years.
# Golden Label: neutral

ratio_premise = 8/2
ratio_hypothesis = 4/2
rahul_age_future_premise = 22
rahul_age_future_hypothesis = 22

# the hypothesis refers to the ratio between Rahul and Deepak and Rahul's age after 6 years, both mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the hypothesis ratio contradicts the premise ratio
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if the hypothesis value for Rahul's age after 6 years contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

