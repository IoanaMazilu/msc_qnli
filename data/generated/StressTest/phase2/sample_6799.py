# Premise: Robert purchased $more than 3000 worth of US saving bonds.
# Hypothesis: Robert purchased $4000 worth of US saving bonds.
# Golden Label: neutral

bonds_purchased_premise = 3000
bonds_purchased_hypothesis = 4000

# the hypothesis refers to the amount of US saving bonds purchased by Robert, which is also mentioned in the premise
if bonds_purchased_hypothesis <= bonds_purchased_premise:
    # check if the hypothesis value contradicts the estimate of more than 'bonds_purchased_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of US saving bonds
    # any amount greater than 'bonds_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

