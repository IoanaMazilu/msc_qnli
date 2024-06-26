bright_score_premise = 60
bright_score_hypothesis = 40
bivi_score_premise = 65
bivi_score_hypothesis = 65
lisa_score_premise = 45
lisa_score_hypothesis = 45

# the hypothesis refers to the score of Bright, which is mentioned in the premise
if bright_score_hypothesis <= bright_score_premise:
    # check if the estimate of 'bright_score_hypothesis' contradicts the score of Bright in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the score of Bright
    # any score greater than 'bright_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
