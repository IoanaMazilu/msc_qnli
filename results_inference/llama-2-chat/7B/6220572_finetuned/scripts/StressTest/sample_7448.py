ratio_premise = 4/3
ratio_hypothesis = 2/3
rahul_age_premise = 26
rahul_age_hypothesis = 26

# the hypothesis talks about the ratio between Rahul and Deepak, referenced also in the premise
if ratio_hypothesis == ratio_premise:
    # check if the hypothesis value contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_hypothesis!= rahul_age_premise:
    # check if the estimated age of Rahul in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio and the age of Rahul
    # any ratio and age consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
