# Premise: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 18 years.
# Hypothesis: Ratio between Rahul and Deepak is more than 1:3, After 6 Years Rahul age will be 18 years.
# Golden Label: entailment

rahul_deepak_ratio_premise = 4 / 3
rahul_deepak_ratio_hypothesis = 1 / 3
rahul_age_future_premise = 18
rahul_age_future_hypothesis = 18

# the hypothesis refers to the ratio between Rahul and Deepak and Rahul's future age, mentioned also in the premise
if rahul_deepak_ratio_premise <= rahul_deepak_ratio_hypothesis:
    # check if the 'rahul_deepak_ratio_hypothesis' contradicts the ratio between Rahul and Deepak in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if Rahul's future age in the hypothesis contradicts Rahul's future age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

