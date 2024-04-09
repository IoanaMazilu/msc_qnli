anita_goes_away_premise = 7
indu_leaves_premise = 7
anita_goes_away_hypothesis = 10
indu_leaves_hypothesis = 15

# the hypothesis talks about the number of days Anita and Indu leave before the work is finished
if anita_goes_away_hypothesis > anita_goes_away_premise and indu_leaves_hypothesis > indu_leaves_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif anita_goes_away_hypothesis == anita_goes_away_premise and indu_leaves_hypothesis == indu_leaves_premise:
    # check if the hypothesis values do not contradict the premise ones
    label = "neutral"
else:
    # the premise gives only an estimate for the number of days Anita and Indu leave
    # any number of days greater than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
