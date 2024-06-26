bright_score_premise = 60
bright_score_hypothesis = 40
bivi_score_premise = 65
bivi_score_hypothesis = 65
lisa_score_premise = 45
lisa_score_hypothesis = 45

# the hypothesis talks about the scores of the three students in the exam
if bright_score_hypothesis <= bright_score_premise:
    # check if the hypothesis value contradicts the estimate of more than 'bright_score_premise'
    label = "contradiction"
elif bivi_score_hypothesis!= bivi_score_premise:
    # check if the number of scored pies in the hypothesis contradicts the number of scored pies reported in the premise
    label = "contradiction"
elif lisa_score_hypothesis!= lisa_score_premise:
    # check if the number of scored pies in the hypothesis contradicts the number of scored pies reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of roses
    # any number of roses greater than 'roses_vase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
