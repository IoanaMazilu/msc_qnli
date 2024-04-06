# Premise: City thrashed West Bromwich Albion 4-0 at the Etihad Stadium to cut United's lead to five points with five games to go.
# Hypothesis: Manchester City cut the gap to five points at the top.
# Golden Label: neutral

city_score_premise = 4
albion_score_premise = 0
united_lead_premise = 5
remaining_games_premise = 5

united_lead_hypothesis = 5

# the hypothesis mentions the five-point gap at the top which is also referenced in the premise
# however, the hypothesis does not refer to the score of the game or the number of remaining games, which cannot be entailed from the premise
if united_lead_hypothesis != united_lead_premise:
    # check if the lead gap in the hypothesis contradicts the lead gap reported in the premise
    label = "contradiction"
else:
    # if the lead gap in the hypothesis does not contradict the lead gap in the premise, but other details are missing, we can infer neutrality
    label = "neutral"

print(label)

