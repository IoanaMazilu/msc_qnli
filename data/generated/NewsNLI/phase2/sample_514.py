# Premise: Cristiano Ronaldo for Real Madrid and Paris Saint Germain's Zlatan Ibrahimovic topped the bill for a prestige friendly, which Real won 1-0.
# Hypothesis: Real Madrid beat Paris Saint Germain 1-0 in friendly in Qatar.
# Golden Label: neutral

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

