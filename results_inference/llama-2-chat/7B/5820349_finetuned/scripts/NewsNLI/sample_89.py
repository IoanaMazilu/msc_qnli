reward_premise = 5000000
reward_hypothesis = 5000000

# the hypothesis mentions the reward offered by the State Department, which is also mentioned in the premise
# however, the hypothesis introduces additional information about the person being wanted in the United States
# this additional information cannot be entailed from the premise, so the relation is neutral
label = "neutral"

print(label)
