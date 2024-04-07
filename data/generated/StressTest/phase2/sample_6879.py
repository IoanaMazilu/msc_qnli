# Premise: Q:Robert purchased $1500 worth of US saving bonds.
# Hypothesis: Q:Robert purchased $less than 6500 worth of US saving bonds.
# Golden Label: entailment

bonds_purchased_premise = 1500
bonds_purchased_hypothesis = 6500

# the hypothesis refers to the value of US bonds purchased by Robert, mentioned also in the premise
if bonds_purchased_hypothesis < bonds_purchased_premise:
    # check if the hypothesis value contradicts the value of 'bonds_purchased_premise' reported in the premise
    label = "contradiction"
elif bonds_purchased_hypothesis == bonds_purchased_premise:
    # check if the value of US bonds purchased in the hypothesis is exactly the same as in the premise
    label = "entailment"
else:
    # the hypothesis gives an upper limit for the value of US bonds purchased by Robert
    # the value from the premise is consistent with this limit, but cannot be explicitly entailed from the hypothesis, so the relationship is neutral
    label = "neutral"

print(label)

