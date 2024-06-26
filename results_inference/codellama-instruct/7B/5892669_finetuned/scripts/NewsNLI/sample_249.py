reward_premise = 5000000
reward_hypothesis = 5000000

# the hypothesis mentions the $5 million reward offered by the U.S. State Department, which is also mentioned in the premise
if reward_hypothesis!= reward_premise:
    # check if the reward value in the hypothesis contradicts the reward value reported in the premise
    label = "contradiction"
else:
    # if the reward value in the hypothesis does not contradict the reward value in the premise, we can infer entailment
    label = "entailment"

print(label)