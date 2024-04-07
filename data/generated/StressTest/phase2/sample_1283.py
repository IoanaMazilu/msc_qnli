# Premise: Q:Robert purchased $3500 worth of US saving bonds.
# Hypothesis: Q:Robert purchased $5500 worth of US saving bonds.
# Golden Label: contradiction

bonds_purchased_premise = 3500
bonds_purchased_hypothesis = 5500

# the hypothesis talks about the amount of US saving bonds Robert purchased, which is also mentioned in the premise
if bonds_purchased_hypothesis != bonds_purchased_premise:
    # check if the value of 'bonds_purchased_hypothesis' contradicts the amount of bonds purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

