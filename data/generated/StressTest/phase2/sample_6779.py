# Premise: In an exam, Bright scored 60 percent, Bivi scored 65 percent and Lisa 45 percent.
# Hypothesis: In an exam, Bright scored more than 60 percent, Bivi scored 65 percent and Lisa 45 percent.
# Golden Label: contradiction

bright_score_premise = 60
bright_score_hypothesis = 60
bivi_score_premise = 65
bivi_score_hypothesis = 65
lisa_score_premise = 45
lisa_score_hypothesis = 45

# the hypothesis refers to the exam scores of Bright, Bivi and Lisa mentioned in the premise
if bright_score_hypothesis > bright_score_premise:
    # check if the score of 'bright_score_hypothesis' contradicts the score of Bright in the premise
    label = "contradiction"
elif (bivi_score_hypothesis != bivi_score_premise) or (lisa_score_hypothesis != lisa_score_premise):
    # check if Bivi's or Lisa's scores in the hypothesis contradict their scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

