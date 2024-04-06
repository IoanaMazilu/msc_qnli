# Premise: In the Spanish Primera, the battle for third place intensified as nine-man Valencia lost 4-1 at Athletico Madrid.
# Hypothesis: Nine-man Valencia thrashed 4-1 by Atletico Madrid in Spanish La Liga.
# Golden Label: entailment

valencia_players_premise = 9
valencia_players_hypothesis = 9
valencia_score_premise = 1
valencia_score_hypothesis = 1
atletico_score_premise = 4
atletico_score_hypothesis = 4

# the hypothesis mentions the number of Valencia players, the score of Valencia and the score of Atletico Madrid, which are also mentioned in the premise
if valencia_players_hypothesis != valencia_players_premise:
    # check if the number of Valencia players in the hypothesis contradicts the number of Valencia players reported in the premise
    label = "contradiction"
elif valencia_score_hypothesis != valencia_score_premise:
    # check if the score of Valencia from the hypothesis contradicts the score of Valencia in the premise
    label = "contradiction"
elif atletico_score_hypothesis != atletico_score_premise:
    # check if the score of Atletico Madrid from the hypothesis contradicts the score of Atletico Madrid in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

