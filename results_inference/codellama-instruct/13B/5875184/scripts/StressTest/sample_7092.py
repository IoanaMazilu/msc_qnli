ratio_premise = 5/2
ratio_hypothesis = 8/2
age_premise = 26
age_hypothesis = 26

# the hypothesis talks about the ratio between Rahul and Deepak, referenced also in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
