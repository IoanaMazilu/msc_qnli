real_madrid_score_premise = 1
real_madrid_score_hypothesis = 1
psg_score_premise = 0
psg_score_hypothesis = 0

# the hypothesis mentions the game result between Real Madrid and Paris Saint Germain, which is also mentioned in the premise
if real_madrid_score_hypothesis != real_madrid_score_premise:
    # check if the score of Real Madrid in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif psg_score_hypothesis != psg_score_premise:
    # check if the score of Paris Saint Germain from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
