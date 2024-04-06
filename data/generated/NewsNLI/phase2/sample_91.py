# Premise: 13 Sara Errani as the Italian came through 6-0 0-6 7-6.
# Hypothesis: Italian world No. 13 Sara Errani wins epic encounter 6-0 0-6 7-6.
# Golden Label: neutral

sara_rank_premise = 13
sara_rank_hypothesis = 13
score_premise = [6, 0, 0, 6, 7, 6]
score_hypothesis = [6, 0, 0, 6, 7, 6]

# The hypothesis mentions the rank and the score of Sara Errani, which are also mentioned in the premise
if sara_rank_hypothesis != sara_rank_premise:
    # check if the rank of Sara Errani in the hypothesis contradicts the rank reported in the premise
    label = "contradiction"
elif score_hypothesis != score_premise:
    # check if the score from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

