# years John will be twice as old as Frank
john_frank_age_ratio_premise = 8
john_frank_age_ratio_hypothesis = 8

# the hypothesis talks about the age ratio between John and Frank in less than 8 years
# the premise talks about the age ratio in 5 years
if john_frank_age_ratio_hypothesis > john_frank_age_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio in the premise
    label = "contradiction"
elif john_frank_age_ratio_hypothesis < john_frank_age_ratio_premise:
    # check if the age ratio in the hypothesis is less than the age ratio in the premise
    label = "entailment"
else:
    # if the age ratio in the hypothesis is equal to the age ratio in the premise, we have a neutral case
    label = "neutral"

print(label)
