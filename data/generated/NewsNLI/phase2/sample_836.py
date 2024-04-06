# Premise: '' Having a chance to win $10 million and our first child on the way -- it's pretty amazing.''
# Hypothesis: Golfer is in contention to win the $10 million FedEx Cup prize.
# Golden Label: neutral

prize_premise = 10000000
prize_hypothesis = 10000000

# the hypothesis mentions the value of the prize, which is also mentioned in the premise
# however, the hypothesis refers to a specific competition (FedEx Cup), which cannot be entailed from the premise
label = "neutral"

print(label)

