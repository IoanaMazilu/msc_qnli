# Premise: Ratio between Rahul and Deepak is more than 3:3, After 6 Years Rahul age will be 22 years.
# Hypothesis: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 22 years.
# Golden Label: neutral

ratio_premise = 3.0/3
ratio_hypothesis = 4.0/3
rahul_age_future_premise = 22
rahul_age_future_hypothesis = 22

# the hypothesis refers to the ratio between Rahul and Deepak, as well as Rahul's future age, both mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the ratio in the hypothesis contradicts the estimate of more than 'ratio_premise'
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    # Rahul's future age is consistent with the premise
    label = "neutral"

print(label)

