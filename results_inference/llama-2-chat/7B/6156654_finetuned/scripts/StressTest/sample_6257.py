discount_premise = 20
discount_hypothesis = 50

# The hypothesis talks about the discount percentage Saren negotiated, which is also mentioned in the premise
if discount_hypothesis == discount_premise:
    label = "entailment"
elif discount_hypothesis < discount_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
