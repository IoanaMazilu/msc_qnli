# Premise: Ratio between Rahul and Deepak is less than 5:3, After 6 Years Rahul age will be 50 years.
# Hypothesis: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 50 years.
# Golden Label: neutral

rahul_deepak_ratio_premise = 5/3
rahul_deepak_ratio_hypothesis = 4/3
rahul_age_future_premise = 50
rahul_age_future_hypothesis = 50

# the hypothesis refers to the ratio between Rahul and Deepak and Rahul's future age, both mentioned in the premise
if rahul_deepak_ratio_hypothesis >= rahul_deepak_ratio_premise:
    # check if the suggested 'rahul_deepak_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if the future age of Rahul in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # if the values in the hypothesis do not contradict the premise ones, we have entailment
    label = "entailment"

print(label)

