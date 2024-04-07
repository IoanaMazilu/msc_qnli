# Premise: Ratio between Rahul and Deepak is less than 7:3, After 2 Years Rahul age will be 26 years.
# Hypothesis: Ratio between Rahul and Deepak is 4:3, After 2 Years Rahul age will be 26 years.
# Golden Label: neutral

rahul_deepak_ratio_premise = 7/3
rahul_deepak_ratio_hypothesis = 4/3

rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# the hypothesis talks about the ratio between Rahul and Deepak and the future age of Rahul, both referenced in the premise
if rahul_deepak_ratio_hypothesis >= rahul_deepak_ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than 'rahul_deepak_ratio_premise'
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio and the future age of Rahul
    # the values in the hypothesis do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

