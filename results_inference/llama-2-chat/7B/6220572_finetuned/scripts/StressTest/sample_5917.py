score_premise = 7
score_hypothesis = 2

# the hypothesis refers to the score Jerry needs to earn to raise his average by 2 points
if score_hypothesis >= score_premise:
    # check if the estimate of'score_hypothesis' contradicts the number of points Jerry needs to raise his average in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of points needed to raise the average
    # any number of points less than'score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
