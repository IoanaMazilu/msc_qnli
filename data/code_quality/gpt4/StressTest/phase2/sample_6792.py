dibi_score_premise = 25
balan_score_premise = 38
cristen_score_premise = 23

dibi_score_hypothesis = 35
balan_score_hypothesis = 38
cristen_score_hypothesis = 23

# the hypothesis talks about the scores of Dibi, Balan and Cristen in an exam, referenced also in the premise
if dibi_score_hypothesis <= dibi_score_premise:
    # check if the hypothesis value contradicts the score of Dibi in the premise
    label = "contradiction"
elif balan_score_hypothesis != balan_score_premise:
    # check if the score of Balan in the hypothesis contradicts the score of Balan in the premise
    label = "contradiction"
elif cristen_score_hypothesis != cristen_score_premise:
    # check if the score of Cristen in the hypothesis contradicts the score of Cristen in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
