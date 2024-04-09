pounds_borrowed_premise = 6500
pounds_borrowed_hypothesis = 1500

# the hypothesis talks about the amount of pounds borrowed for college education, which is also mentioned in the premise
if pounds_borrowed_hypothesis <= pounds_borrowed_premise:
    # check if the hypothesis value contradicts the estimate of 'pounds_borrowed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of pounds borrowed
    # any amount of pounds borrowed greater than 'pounds_borrowed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
