age_arun_premise = 5
age_deepak_premise = 4
age_arun_hypothesis = 1
age_deepak_hypothesis = 4

# the hypothesis talks about the ratio between the ages of Arun and Deepak
if age_arun_hypothesis <= age_arun_premise:
    # check if the hypothesis value contradicts the estimate of more than 'age_arun_premise'
    label = "contradiction"
elif age_deepak_hypothesis!= age_deepak_premise:
    # check if the number of deepak's age in the hypothesis contradicts the number of deepak's age reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between the ages of Arun and Deepak
    # any ratio between the ages of Arun and Deepak greater than 'age_arun_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
