age_arun_premise = 3
age_deepak_premise = 3
age_arun_hypothesis = 4
age_deepak_hypothesis = 3

# the hypothesis refers to the ratio between the ages of Arun and Deepak
if age_arun_hypothesis / age_deepak_hypothesis > age_arun_premise / age_deepak_premise:
    # check if the estimate of 'age_arun_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif age_arun_hypothesis / age_deepak_hypothesis == age_arun_premise / age_deepak_premise:
    # check if the estimate of 'age_arun_hypothesis' is consistent with the ratio in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the ratio
    # any ratio greater than 'age_arun_premise / age_deepak_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
