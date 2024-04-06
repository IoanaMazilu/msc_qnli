# Premise: See all of the U.S. beachfront hotels under $200.
# Hypothesis: California offers a crop of beachfront hotels under $200.
# Golden Label: neutral

hotel_price_premise = 200
hotel_price_hypothesis = 200

# the hypothesis mentions the price of beachfront hotels in California, which is a subset of the U.S. beachfront hotels mentioned in the premise
# however, the premise does not specify whether there are beachfront hotels under $200 in California specifically
if hotel_price_hypothesis > hotel_price_premise:
    # check if the hotel price in the hypothesis contradicts the hotel price in the premise
    label = "contradiction"
else:
    # if the hotel price in the hypothesis does not contradict the hotel price in the premise, we cannot infer entailment or contradiction
    label = "neutral"

print(label)

