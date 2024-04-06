# Premise: The roommates found more envelopes in the couch, which they had bought at the Salvation Army for $20.
# Hypothesis: Three roommates bought a couch at the Salvation Army for $20.
# Golden Label: neutral

couch_price_premise = 20
couch_price_hypothesis = 20

# Both the premise and hypothesis mention the price of a couch bought at the Salvation Army
# However, the number of roommates who bought the couch is not mentioned in the premise
# Therefore, we cannot infer "entailment" or "contradiction" based on the provided information
label = "neutral"

print(label)

