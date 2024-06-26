us_reward_premise = 5000000
us_reward_hypothesis = 5000000

# the hypothesis mentions the U.S. reward for his capture, which is also mentioned in the premise
if us_reward_hypothesis!= us_reward_premise:
    # check if the U.S. reward in the hypothesis contradicts the U.S. reward in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
