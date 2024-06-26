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
elif bivi_score_hypothesis!= bivi_score_premise or lisa_score_hypothesis!= lisa_score_premise:
    # check if the scores of Bivi or Lisa in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Bright's score
    # Bright's score in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
