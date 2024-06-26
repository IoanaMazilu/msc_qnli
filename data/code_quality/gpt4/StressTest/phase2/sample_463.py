borrowed_amount_premise = 8700
borrowed_amount_hypothesis = 5700

# the hypothesis refers to the total amount borrowed by Albert from Brian and Charlie
if borrowed_amount_hypothesis >= borrowed_amount_premise:
    # check if the amount in the hypothesis contradicts the premise stating Albert borrowed less than 'borrowed_amount_premise'
    label = "contradiction"
elif borrowed_amount_hypothesis < borrowed_amount_premise:
    # the premise gives only an upper limit for the borrowed amount
    # any amount less than 'borrowed_amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
