bright_premise = 40
bright_hypothesis = 60
bivi_premise = 65
bivi_hypothesis = 65
lisa_premise = 45
lisa_hypothesis = 45

# the hypothesis refers to the scores of Bright, Bivi and Lisa mentioned in the premise
if bright_hypothesis <= bright_premise:
    # check if the estimate of 'bright_hypothesis' contradicts the score of Bright in the premise
    label = "contradiction"
elif bivi_hypothesis!= bivi_premise:
    # check if the score of Bivi in the hypothesis contradicts the score of Bivi reported in the premise
    label = "contradiction"
elif lisa_hypothesis!= lisa_premise:
    # check if the score of Lisa in the hypothesis contradicts the score of Lisa reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
