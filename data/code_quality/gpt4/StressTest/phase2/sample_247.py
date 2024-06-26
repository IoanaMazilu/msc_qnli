ratio_rahul_deepak_premise = 2/3
ratio_rahul_deepak_hypothesis = 4/3

rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# The hypothesis refers to the ratio between Rahul and Deepak mentioned in the premise
if ratio_rahul_deepak_hypothesis <= ratio_rahul_deepak_premise:
    # Check if the 'ratio_rahul_deepak_hypothesis' contradicts the ratio of Rahul and Deepak in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # Check if the future age of Rahul in the hypothesis contradicts the future age of Rahul stated in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
