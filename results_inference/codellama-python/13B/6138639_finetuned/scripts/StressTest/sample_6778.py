bright_score_premise = 40
bright_score_hypothesis = 60
bivi_score_premise = 65
bivi_score_hypothesis = 65
lisa_score_premise = 45
lisa_score_hypothesis = 45

# the hypothesis talks about the scores of Bright, Bivi and Lisa in an exam, referenced also in the premise
if bright_score_hypothesis <= bright_score_premise:
    # check if the hypothesis value contradicts the estimate of more than 'bright_score_premise'
    label = "contradiction"
elif bivi_score_hypothesis!= bivi_score_premise:
    # check if the score of Bivi in the hypothesis contradicts the score of Bivi reported in the premise
    label = "contradiction"
elif lisa_score_hypothesis!= lisa_score_premise:
    # check if the score of Lisa in the hypothesis contradicts the score of Lisa reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the score of Bright
    # any score of Bright greater than 'bright_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
