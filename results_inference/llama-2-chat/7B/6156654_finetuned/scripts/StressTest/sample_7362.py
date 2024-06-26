discount_premise = 30
discount_hypothesis = 10

# the hypothesis talks about the discount on the listed price, which is also mentioned in the premise
if discount_premise <= discount_hypothesis:
    # check if the discount in the hypothesis contradicts the discount in the premise
    label = "contradiction"
elif discount_premise > discount_hypothesis:
    # if the discount in the premise is greater than the discount in the hypothesis, it entails the hypothesis
    label = "entailment"
else:
    # if the discount in the premise is equal to the discount in the hypothesis, it is neutral
    label = "neutral"

print(label)
