# Premise: A $25,000 reward is offered.
# Hypothesis: Have a tip? Call 352-367-4161. A $25,000 reward is offered.
# Golden Label: entailment

reward_premise = 25000
reward_hypothesis = 25000

# The hypothesis mentions the amount of the reward which is also mentioned in the premise.
if reward_hypothesis != reward_premise:
    # Check if the reward amount in the hypothesis contradicts the reward amount in the premise.
    label = "contradiction"
else:
    # If the reward amount in the hypothesis does not contradict the reward amount in the premise, we can infer entailment.
    label = "entailment"

print(label)

