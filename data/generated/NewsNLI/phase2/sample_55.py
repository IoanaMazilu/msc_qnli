# Premise: The new system will have two national semifinal games and a final.
# Hypothesis: There will be two national semifinal games and a final, with teams selected by a committee.
# Golden Label: neutral

semifinal_games_premise = 2
final_game_premise = 1
semifinal_games_hypothesis = 2
final_game_hypothesis = 1

# the hypothesis mentions the number of national semifinal games and the final, which are also mentioned in the premise
# however, the hypothesis also refers to the selection of teams by a committee, which cannot be entailed from the premise
label = "neutral"

print(label)

