offer_percentage_premise = 20
offer_percentage_hypothesis = 80
shirt_purchased_premise = 20
shirt_purchased_hypothesis = 20

# the hypothesis talks about the offer percentage and the purchase of a shirt, which are also mentioned in the premise
if offer_percentage_premise <= offer_percentage_hypothesis and shirt_purchased_premise <= shirt_purchased_hypothesis:
    # check if the hypothesis value contradicts the premise values
    label = "contradiction"
elif offer_percentage_hypothesis < offer_percentage_premise and shirt_purchased_hypothesis < shirt_purchased_premise:
    # check if the hypothesis values are less than the premise values but do not contradict them
    label = "neutral"
else:
    # if the hypothesis values are greater than or equal to the premise values, and do not contradict them, we can infer entailment
    label = "entailment"

print(label)
