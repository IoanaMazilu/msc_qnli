dibi_score_premise = 25
dibi_score_hypothesis = 35
balan_score_premise = 38
balan_score_hypothesis = 38
cristen_score_premise = 23
cristen_score_hypothesis = 23

# the hypothesis refers to the scores of Dibi and Cristen, mentioned in the premise
if dibi_score_hypothesis >= dibi_score_premise:
    # check if the hypothesis value contradicts the score of Dibi in the premise
    label = "contradiction"
elif cristen_score_hypothesis!= cristen_score_premise:
    # check if the score of Cristen in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
