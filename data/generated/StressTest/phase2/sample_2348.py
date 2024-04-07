# Premise: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 42 years.
# Hypothesis: Ratio between Rahul and Deepak is less than 4:3, After 6 Years Rahul age will be 42 years.
# Golden Label: contradiction

ratio_premise = 4/3
ratio_hypothesis = 4/3
rahul_age_future_premise = 42
rahul_age_future_hypothesis = 42

# the hypothesis refers to the ratio between Rahul and Deepak and Rahul's future age mentioned in the premise
if ratio_hypothesis > ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age mentioned in the premise
    label = "contradiction"
elif ratio_hypothesis < ratio_premise:
    # if the ratio in the hypothesis is less than the ratio in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

