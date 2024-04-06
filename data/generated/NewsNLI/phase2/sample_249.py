# Premise: Among the nations seeking him was the United States, which had offered a $5 million reward to anyone who helped bring about his capture.
# Hypothesis: U.S. State Department had offered a $5 million reward for his arrest.
# Golden Label: entailment

reward_premise = 5000000
reward_hypothesis = 5000000

# the hypothesis mentions the reward offered by the U.S. which is also mentioned in the premise
if reward_hypothesis != reward_premise:
    # check if the reward in the hypothesis contradicts the reward mentioned in the premise
    label = "contradiction"
else:
    # if the reward value in the hypothesis does not contradict the reward value in the premise, we can infer entailment
    label = "entailment"

print(label)

