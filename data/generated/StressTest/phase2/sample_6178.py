# Premise: Ratio between Rahul and Deepak is less than 6:3, After 6 Years Rahul age will be 34 years.
# Hypothesis: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 34 years.
# Golden Label: neutral

ratio_premise = 6/3
ratio_hypothesis = 4/3
rahul_age_premise = 34
rahul_age_hypothesis = 34

# the hypothesis talks about the ratio between Rahul and Deepak, and Rahul's age after 6 years, both mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the hypothesis ratio contradicts the premise ratio
    label = "contradiction"
elif rahul_age_hypothesis != rahul_age_premise:
    # check if Rahul's age in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

