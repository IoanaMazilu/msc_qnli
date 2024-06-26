ratio_rahul_deepak_premise = 4/3
ratio_rahul_deepak_hypothesis = 6/3

# the hypothesis talks about the ratio between Rahul and Deepak, referenced also in the premise
if ratio_rahul_deepak_hypothesis <= ratio_rahul_deepak_premise:
    # check if the hypothesis value contradicts the estimate of 'ratio_rahul_deepak_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between Rahul and Deepak
    # any ratio greater than 'ratio_rahul_deepak_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
