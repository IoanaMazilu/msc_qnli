# Premise: Ratio between Rahul and Deepak is 4:3, After 10 Years Rahul age will be 26 years.
# Hypothesis: Ratio between Rahul and Deepak is more than 2:3, After 10 Years Rahul age will be 26 years.
# Golden Label: entailment

rahul_deepak_ratio_premise = 4/3
rahul_deepak_ratio_hypothesis = 2/3
rahul_future_age_premise = 26
rahul_future_age_hypothesis = 26

# the hypothesis discusses the ratio of ages between Rahul and Deepak, and Rahul's future age
if rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # check if the hypothesis ratio contradicts the ratio in the premise
    label = "contradiction"
elif rahul_future_age_hypothesis != rahul_future_age_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

