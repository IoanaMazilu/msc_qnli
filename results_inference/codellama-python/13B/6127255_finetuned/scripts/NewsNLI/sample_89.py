reward_premise = 5000000
reward_hypothesis = 5000000

# the hypothesis mentions the amount of the reward offered by the State Department, which is also mentioned in the premise
if reward_hypothesis!= reward_premise:
    # check if the reward amount in the hypothesis contradicts the reward amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis reward amount does not contradict the premise reward amount, we can infer entailment
    label = "entailment"

print(label)
