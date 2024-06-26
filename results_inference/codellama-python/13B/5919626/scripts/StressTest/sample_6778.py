bright_score_premise = 40
bright_score_hypothesis = 60
bivi_score_premise = 65
bivi_score_hypothesis = 65
lisa_score_premise = 45
lisa_score_hypothesis = 45

# the hypothesis refers to the number of scored points in the exam
if bright_score_premise <= bright_score_hypothesis:
    # check if the estimate of 'bright_score_hypothesis' contradicts the number of scored points in the premise
    label = "contradiction"
elif bivi_score_hypothesis!= bivi_score_premise:
    # check if the number of scored points in the hypothesis contradicts the number of scored points in the premise
    label = "contradiction"
elif lisa_score_hypothesis!= lisa_score_premise:
    # check if the number of scored points in the hypothesis contradicts the number of scored points in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
