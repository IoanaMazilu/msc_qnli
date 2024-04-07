# Premise: Q:Robert purchased $1500 worth of US saving bonds.
# Hypothesis: Q:Robert purchased $7500 worth of US saving bonds.
# Golden Label: contradiction

bonds_purchased_premise = 1500
bonds_purchased_hypothesis = 7500

# the hypothesis refers to the amount of US saving bonds purchased by Robert as mentioned in the premise
if bonds_purchased_hypothesis != bonds_purchased_premise:
    # check if the value of 'bonds_purchased_hypothesis' contradicts the amount of bonds purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

