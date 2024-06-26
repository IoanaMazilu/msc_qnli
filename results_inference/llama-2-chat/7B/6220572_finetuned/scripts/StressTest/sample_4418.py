average_raising_premise = 2
average_raising_hypothesis = 5

# the hypothesis refers to the number of points needed to raise Jerry's average, referenced also in the premise
if average_raising_hypothesis!= average_raising_premise:
    # check if the hypothesis value contradicts the estimate of 'average_raising_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of points needed to raise Jerry's average
    # any number of points greater than 'average_raising_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
