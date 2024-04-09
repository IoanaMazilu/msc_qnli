lewis_age_premise = 1
brown_age_premise = 2
lewis_age_hypothesis = 0.5
brown_age_hypothesis = 1.5

# the hypothesis refers to the ratio of their ages
if lewis_age_hypothesis * brown_age_hypothesis > (lewis_age_premise * brown_age_premise):
    # check if the estimate of the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif lewis_age_hypothesis * brown_age_hypothesis <= (lewis_age_premise * brown_age_premise):
    # check if the estimate of the ratio in the hypothesis is consistent with the ratio in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
