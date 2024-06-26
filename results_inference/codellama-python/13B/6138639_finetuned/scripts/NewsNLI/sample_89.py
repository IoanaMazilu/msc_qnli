reward_premise = 5000000
reward_hypothesis = 5000000

# the hypothesis mentions the reward offered by the State Department, which is also mentioned in the premise
if reward_hypothesis!= reward_premise:
    # check if the reward in the hypothesis contradicts the reward reported in the premise
    label = "contradiction"
else:
    # if the reward in the hypothesis does not contradict the reward in the premise, we can infer entailment
    label = "entailment"

print(label)
