# Premise: Albert borrowed a total of $more than 4000 from john and Charlie.
# Hypothesis: Albert borrowed a total of $6000 from john and Charlie.
# Golden Label: neutral

amount_borrowed_premise = 4000
amount_borrowed_hypothesis = 6000

# the hypothesis refers to the total amount that Albert borrowed from John and Charlie, also mentioned in the premise
if amount_borrowed_hypothesis <= amount_borrowed_premise:
    # check if the 'amount_borrowed_hypothesis' contradicts the premise of amount being more than 'amount_borrowed_premise'
    label = "contradiction"
else:
    # the premise only gives an estimate for the amount borrowed
    # any amount greater than 'amount_borrowed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

