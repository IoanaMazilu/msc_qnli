ratio_premise = 5
ratio_hypothesis = 8
age_premise = 26

# the hypothesis talks about the ratio between Rahul and Deepak, and the age of Rahul after 6 years
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
elif ratio_hypothesis > ratio_premise:
    # check if the hypothesis value entails the estimate of the ratio in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the ratio
    # any ratio less than 8:2 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

# the hypothesis also mentions the age of Rahul after 6 years, which is consistent with the premise
# so we can infer entailment

print(label)
