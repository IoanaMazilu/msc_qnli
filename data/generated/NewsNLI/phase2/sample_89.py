# Premise: The State Department has offered a $5 million reward for his capture.
# Hypothesis: He was also wanted in the United States, and the State Department had offered a $5 million reward for his capture.
# Golden Label: neutral

reward_premise = 5000000
reward_hypothesis = 5000000

# the hypothesis mentions the reward offered by the State Department for capture, which is also referenced in the premise
# however, the hypothesis also mentions that he was wanted in the United States, which cannot be entailed from the premise
label = "neutral"

print(label)

