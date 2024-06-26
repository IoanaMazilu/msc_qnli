bright_score_premise = 60
bright_score_hypothesis = 60
bivi_score_premise = 65
bivi_score_hypothesis = 65
lisa_score_premise = 45
lisa_score_hypothesis = 45

# the hypothesis refers to the scores mentioned in the premise
if bright_score_hypothesis <= bright_score_premise:
    # check if the estimate of 'bright_score_hypothesis' contradicts the score of Bright in the premise
    label = "contradiction"
elif bivi_score_hypothesis!= bivi_score_premise:
    # check if the score of Bivi in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif lisa_score_hypothesis!= lisa_score_premise:
    # check if the score of Lisa in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
