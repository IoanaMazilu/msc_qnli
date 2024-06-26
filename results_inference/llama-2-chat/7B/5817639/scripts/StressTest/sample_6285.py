score_premise = float(input("Enter Robin's score on the 10th test: "))
score_hypothesis = float(input("Enter Robin's score on a less than 70th test: "))

# the hypothesis talks about the score on a less than 70th test, which is referenced in the premise
if score_hypothesis <= score_premise:
    # check if the hypothesis value contradicts the estimate of the score in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the score, any score greater than'score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
