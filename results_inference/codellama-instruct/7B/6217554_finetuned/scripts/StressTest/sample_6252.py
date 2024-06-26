# define variables for the scores in the premise and hypothesis
score_1_premise = 1
score_2_premise = 2
score_3_premise = 3
score_4_premise = 4
score_1_hypothesis = 7
score_2_hypothesis = 2
score_3_hypothesis = 3
score_4_hypothesis = 4

# the hypothesis refers to the scores mentioned in the premise
if score_1_hypothesis <= score_1_premise:
    # check if the estimate of'score_1_hypothesis' contradicts the score 1 in the premise
    label = "contradiction"
elif score_2_hypothesis!= score_2_premise:
    # check if the score 2 in the hypothesis contradicts the score 2 reported in the premise
    label = "contradiction"
elif score_3_hypothesis!= score_3_premise:
    # check if the score 3 in the hypothesis contradicts the score 3 reported in the premise
    label = "contradiction"
elif score_4_hypothesis!= score_4_premise:
    # check if the score 4 in the hypothesis contradicts the score 4 reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
