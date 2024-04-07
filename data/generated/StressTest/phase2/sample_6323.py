# Premise: There are 4 chess amateurs playing in Villa's chess club tournament.
# Hypothesis: There are more than 4 chess amateurs playing in Villa's chess club tournament.
# Golden Label: contradiction

chess_players_premise = 4
chess_players_hypothesis = 4

# the hypothesis talks about the number of chess players in Villa's chess club tournament, referenced also in the premise
if chess_players_hypothesis != chess_players_premise:
    # check if the hypothesis value contradicts the exact number of 'chess_players_premise'
    label = "contradiction"
else:
    # the premise gives the exact number of chess players
    # any number of chess players equal to 'chess_players_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

