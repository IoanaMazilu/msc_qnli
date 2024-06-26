offer_premise = 25
offer_hypothesis = 45

# the hypothesis talks about the discount offer in a shop, referenced also in the premise
if offer_hypothesis < offer_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif offer_hypothesis > offer_premise:
    # if the hypothesis value does not contradict the premise and is greater, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value equals the premise, it is neutral
    label = "neutral"

print(label)
