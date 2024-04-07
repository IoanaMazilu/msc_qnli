# Premise: Robert purchased $4000 worth of US saving bonds.
# Hypothesis: Robert purchased $more than 3000 worth of US saving bonds.
# Golden Label: entailment

bonds_purchased_premise = 4000
bonds_purchased_hypothesis = 3000

# the hypothesis talks about the amount of US saving bonds that Robert purchased, referenced also in the premise
if bonds_purchased_hypothesis >= bonds_purchased_premise:
    # check if the hypothesis value contradicts the exact amount of 'bonds_purchased_premise'
    label = "contradiction"
else:
    # the hypothesis value is less than the premise value, thus it can be explicitly entailed from the premise
    label = "entailment"

print(label)

