pounds_borrowed_premise = 5000
pounds_borrowed_hypothesis = 3000

# check if the hypothesis value contradicts the estimate of 'pounds_borrowed_premise'
if pounds_borrowed_hypothesis <= pounds_borrowed_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount borrowed
    # any amount borrowed greater than 'pounds_borrowed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
