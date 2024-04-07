# Premise: Ratio between Rahul and Deepak is 4:3, After 2 Years Rahul age will be 26 years.
# Hypothesis: Ratio between Rahul and Deepak is 8:3, After 2 Years Rahul age will be 26 years.
# Golden Label: contradiction

rahul_deepak_ratio_premise = 4 / 3
rahul_deepak_ratio_hypothesis = 8 / 3
rahul_future_age_premise = 26
rahul_future_age_hypothesis = 26

# the hypothesis talks about the ratio between Rahul and Deepak's ages and Rahul's future age
if rahul_future_age_hypothesis != rahul_future_age_premise:
    # check if the age of Rahul in the future contradicts the premise
    label = "contradiction"
elif rahul_deepak_ratio_hypothesis != rahul_deepak_ratio_premise:
    # check if the ratio between Rahul and Deepak's ages in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

