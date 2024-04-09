arun_age_premise = 5
deepak_age_premise = 4
ratio_premise = arun_age_premise / deepak_age_premise

hypothesis_ratio = 1.4

# the hypothesis talks about the ratio of Arun and Deepak's ages
if hypothesis_ratio > ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
elif hypothesis_ratio == ratio_premise:
    # the hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the ratio
    # any ratio greater than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
