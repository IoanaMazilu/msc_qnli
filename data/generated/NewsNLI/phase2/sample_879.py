# Premise: Back in the big time, Frankfurt has made a blistering start to its season, winning its first four games before being held to a 3-3 tie by champion Borussia Dortmund.
# Hypothesis: Eintracht Frankfurt held to a 1-1 draw by Greuther Frth.
# Golden Label: neutral

tie_score_premise = 3
tie_score_hypothesis = 1

# the hypothesis mentions the tie score of Frankfurt's game, which is also referenced in the premise
# however, the hypothesis refers to a different game and different opponent team, which cannot be entailed from the premise
# moreover, the tie score is different from the premise
if tie_score_hypothesis != tie_score_premise:
    # check if the tie score in the hypothesis contradicts the tie score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we would infer neutrality due to different games and opponents
    label = "neutral"

print(label)

