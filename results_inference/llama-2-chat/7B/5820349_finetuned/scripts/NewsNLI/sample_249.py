reward_premise = 500000
reward_hypothesis = 500000

# the hypothesis mentions the reward offered by the U.S. State Department, which is also mentioned in the premise
if reward_hypothesis!= reward_premise:
    # check if the reward in the hypothesis contradicts the reward reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
