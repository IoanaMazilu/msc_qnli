reward_premise = 5000
reward_hypothesis = 5000

# the hypothesis mentions the reward offered, which is also mentioned in the premise
if reward_hypothesis!= reward_premise:
    # check if the reward in the hypothesis contradicts the reward reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
