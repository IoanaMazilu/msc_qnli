borrowed_premise = 5000
borrowed_hypothesis = 2000

# the hypothesis refers to the amount borrowed by Dana for her college education, which is also mentioned in the premise
if borrowed_hypothesis <= borrowed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'borrowed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount borrowed
    # any amount borrowed greater than 'borrowed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
