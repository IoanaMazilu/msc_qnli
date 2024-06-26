score_1_premise = 1
score_2_premise = 2
score_3_premise = 3
score_4_premise = 4
score_5_premise = 5

score_1_hypothesis = 8
score_2_hypothesis = 2
score_3_hypothesis = 3
score_4_hypothesis = 4
score_5_hypothesis = 5

# the hypothesis refers to the scores mentioned in the premise
if score_1_hypothesis <= score_1_premise:
    # check if the hypothesis value contradicts the estimate of'score_1_premise'
    label = "contradiction"
elif score_2_hypothesis!= score_2_premise:
    # check if the score of'score_2_hypothesis' contradicts the score of'score_2_premise'
    label = "contradiction"
elif score_3_hypothesis!= score_3_premise:
    # check if the score of'score_3_hypothesis' contradicts the score of'score_3_premise'
    label = "contradiction"
elif score_4_hypothesis!= score_4_premise:
    # check if the score of'score_4_hypothesis' contradicts the score of'score_4_premise'
    label = "contradiction"
elif score_5_hypothesis!= score_5_premise:
    # check if the score of'score_5_hypothesis' contradicts the score of'score_5_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
