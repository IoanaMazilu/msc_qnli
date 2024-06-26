average_raising_premise = 2
average_raising_hypothesis = 7

# the hypothesis refers to the number of points Jerry must raise his average by, also mentioned in the premise
if average_raising_hypothesis <= average_raising_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_raising_premise'
    label = "contradiction"
else:
    # any number of points less than 'average_raising_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
