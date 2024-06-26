score_premise = (14, 13)
score_hypothesis = (14, 13)
penalties_premise = 15 * 2
penalties_hypothesis = 30

# the hypothesis mentions the shootout score and the total number of penalties, which are also referenced in the premise
if score_hypothesis != score_premise:
    # check if the shootout score in the hypothesis contradicts the shootout score reported in the premise
    label = "contradiction"
elif penalties_hypothesis != penalties_premise:
    # check if the total number of penalties from the hypothesis contradicts the total number of penalties in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
