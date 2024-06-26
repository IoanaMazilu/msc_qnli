score_premise = 18
score_hypothesis = 88

# The hypothesis talks about the score Johnny might get in a course, referenced also in the premise
if score_hypothesis <= score_premise:
    # check if the hypothesis value contradicts the estimate of more than 'score_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the score
    # Any score greater than 'score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
