reward_premise = 5000000
reward_hypothesis = 5000000

# the hypothesis mentions the reward amount offered by the U.S. State Department, which is also mentioned in the premise
if reward_hypothesis!= reward_premise:
    # check if the reward amount in the hypothesis contradicts the reward amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
