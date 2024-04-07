# Premise: Ratio between Rahul and Deepak is 4:2, After 10 Years Rahul age will be 26 years.
# Hypothesis: Ratio between Rahul and Deepak is 6:2, After 10 Years Rahul age will be 26 years.
# Golden Label: contradiction

# defining variables for the premise
ratio_rahul_premise = 4
ratio_deepak_premise = 2
rahul_future_age_premise = 26

# defining variables for the hypothesis
ratio_rahul_hypothesis = 6
ratio_deepak_hypothesis = 2
rahul_future_age_hypothesis = 26

# comparing the ratios between Rahul and Deepak in the premise and hypothesis
if (ratio_rahul_premise/ratio_deepak_premise) != (ratio_rahul_hypothesis/ratio_deepak_hypothesis):
    # if the ratios between Rahul and Deepak in the premise and hypothesis are not the same, it's a contradiction
    label = "contradiction"
elif rahul_future_age_premise != rahul_future_age_hypothesis:
    # if Rahul's future age in the premise and hypothesis is not the same, it's a contradiction
    label = "contradiction"
else:
    # if the ratios and Rahul's future age in the premise and hypothesis are the same, it's an entailment
    label = "entailment"

print(label)

