n_sold_premise = 6
n_sold_hypothesis = 2

# the hypothesis talks about the number of boxes sold by Mark and Ann, referenced also in the premise
if n_sold_hypothesis <= n_sold_premise:
    # check if the hypothesis value contradicts the estimate of 'n_sold_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes sold by Mark and Ann
    # any number of boxes sold by Mark and Ann that is consistent with the premise is neutral, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
