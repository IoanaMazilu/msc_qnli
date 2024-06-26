bright_score_premise = 60
bivi_score_premise = 65
lisa_score_premise = 45

bright_score_hypothesis = 40

# the hypothesis refers to the scores of Bright, Bivi, and Lisa
if bright_score_hypothesis > bright_score_premise:
    # check if the estimate of Bright's score contradicts the premise
    label = "contradiction"
elif bivi_score_hypothesis!= bivi_score_premise:
    # check if the number of Bivi's score in the hypothesis contradicts the premise
    label = "contradiction"
elif lisa_score_hypothesis!= lisa_score_premise:
    # check if the number of Lisa's score in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if all scores in the hypothesis are consistent with the premise, we can infer entailment
    label = "entailment"

print(label)
