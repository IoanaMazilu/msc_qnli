# Premise: Ratio between Rahul and Deepak is 4:3, After 10 Years Rahul age will be 26 years.
# Hypothesis: Ratio between Rahul and Deepak is more than 4:3, After 10 Years Rahul age will be 26 years.
# Golden Label: contradiction

rahul_deepak_ratio_premise = 4/3
rahul_deepak_ratio_hypothesis = 4/3  # implicit from the statement "more than 4:3"

rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# the hypothesis refers to the ratio between Rahul and Deepak's ages and Rahul's future age, both mentioned in the premise
if rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # check if the estimated 'rahul_deepak_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if Rahul's future age in the hypothesis contradicts the future age given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we have a neutral situation
    # since the ratio "more than 4:3" cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

