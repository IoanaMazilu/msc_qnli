# Premise: Q:Robert purchased $1000 worth of US saving bonds.
# Hypothesis: Q:Robert purchased $less than 6000 worth of US saving bonds.
# Golden Label: entailment

bonds_purchased_premise = 1000
bonds_purchased_hypothesis = 6000

# the hypothesis refers to the value of US saving bonds purchased by Robert, also mentioned in the premise
if bonds_purchased_hypothesis < bonds_purchased_premise:
    # check if the hypothesis value contradicts the value of 'bonds_purchased_premise'
    label = "contradiction"
elif bonds_purchased_premise > bonds_purchased_hypothesis:
    # check if the value of 'bonds_purchased_premise' contradicts the hypothesis estimate
    label = "contradiction"
else:
    # the premise value does not contradict the hypothesis estimate
    # any value less than 'bonds_purchased_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "neutral"

print(label)

