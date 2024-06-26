dibi_score_premise = 25
balan_score_premise = 38
cristen_score_premise = 23
dibi_score_hypothesis = 35
balan_score_hypothesis = 38
cristen_score_hypothesis = 23

# the hypothesis talks about the scores of the three students in the exam
if dibi_score_hypothesis <= dibi_score_premise:
    # check if the hypothesis value contradicts the estimate of 'dibi_score_premise'
    label = "contradiction"
elif balan_score_hypothesis!= balan_score_premise:
    # check if the number of scored pies in the hypothesis contradicts the number of scored pies reported in the premise
    label = "contradiction"
elif cristen_score_hypothesis!= cristen_score_premise:
    # check if the number of scored pies in the hypothesis contradicts the number of scored pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
