anita_goes_away_premise = "Anita goes away"
indu_leaves_premise = "Indu leaves 7 days before the work is finished"
anita_goes_away_hypothesis = "Anita goes away"
indu_leaves_hypothesis = "Indu leaves more than 1 days before the work is finished"

# the hypothesis talks about the time gap between Anita going away and Indu leaving
if anita_goes_away_hypothesis <= indu_leaves_premise:
    # check if the hypothesis value contradicts the estimate of 'indu_leaves_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time gap between Anita going away and Indu leaving
    # any time gap greater than 'indu_leaves_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
