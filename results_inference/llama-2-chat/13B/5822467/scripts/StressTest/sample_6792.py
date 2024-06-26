dibi_score_premise = 25
balan_score_premise = 38
cristen_score_premise = 23
dibi_score_hypothesis = 35

# the hypothesis refers to the scores of Dibi, Balan, and Cristen in the exam
if dibi_score_hypothesis <= dibi_score_premise and balan_score_hypothesis == balan_score_premise and cristen_score_hypothesis == cristen_score_premise:
    # check if the hypothesis values for each student contradict the premise values
    label = "contradiction"
elif dibi_score_hypothesis < dibi_score_premise or balan_score_hypothesis!= balan_score_premise or cristen_score_hypothesis!= cristen_score_premise:
    # check if the hypothesis values for any student contradict the premise values
    label = "contradiction"
else:
    # if the hypothesis values for all students do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
