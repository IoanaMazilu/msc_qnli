rahul_deepak_ratio_premise = 4/3
rahul_deepak_ratio_hypothesis = 6/3
rahul_age_premise = 34
rahul_age_hypothesis = 34

# the hypothesis refers to the ratio between Rahul and Deepak, and Rahul's age after 6 years
if rahul_deepak_ratio_premise <= rahul_deepak_ratio_hypothesis and rahul_age_premise == rahul_age_hypothesis:
    # check if the hypothesis values contradict the premise values
    label = "neutral"
elif rahul_deepak_ratio_premise > rahul_deepak_ratio_hypothesis:
    # if the premise ratio is greater than the hypothesis ratio, it entails a contradiction
    label = "contradiction"
else:
    # if the premise and hypothesis ratios are equal, it is neutral
    label = "neutral"

print(label)
