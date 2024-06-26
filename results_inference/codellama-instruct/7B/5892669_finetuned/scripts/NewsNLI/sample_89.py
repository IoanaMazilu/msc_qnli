reward_premise = 500000
reward_hypothesis = 500000

# the hypothesis mentions the amount of the reward offered by the State Department, which is also mentioned in the premise
if reward_hypothesis!= reward_premise:
    # check if the reward amount in the hypothesis contradicts the reward amount reported in the premise
    label = "contradiction"
else:
    # if the reward amount in the hypothesis does not contradict the reward amount in the premise, we can infer entailment
    label = "entailment"

print(label)
