ratio_rahul_premise = 4
ratio_rahul_hypothesis = 2
ratio_deepak_premise = 3
ratio_deepak_hypothesis = 3
age_rahul_premise = 26
age_rahul_hypothesis = 26

# the hypothesis talks about the ratio between Rahul and Deepak, referenced also in the premise
if ratio_rahul_premise!= ratio_rahul_hypothesis:
    # check if the hypothesis value contradicts the estimate of the ratio between Rahul and Deepak in the premise
    label = "contradiction"
elif ratio_deepak_premise!= ratio_deepak_hypothesis:
    # check if the hypothesis value contradicts the estimate of the ratio between Rahul and Deepak in the premise
    label = "contradiction"
elif age_rahul_premise!= age_rahul_hypothesis:
    # check if the hypothesis value contradicts the estimate of the age of Rahul in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between Rahul and Deepak and the age of Rahul
    # any number of roses greater than 'roses_vase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
