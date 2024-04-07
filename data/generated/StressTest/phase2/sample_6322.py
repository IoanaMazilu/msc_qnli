# Premise: There are less than 8 chess amateurs playing in Villa's chess club tournament.
# Hypothesis: There are 4 chess amateurs playing in Villa's chess club tournament.
# Golden Label: neutral

chess_players_premise = 8
chess_players_hypothesis = 4

# the hypothesis mentions a specific number of chess players, while the premise gives an upper limit
if chess_players_hypothesis >= chess_players_premise:
    # check if the number of chess players in the hypothesis contradicts the premise statement of less than 'chess_players_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate (upper bound) for the number of amateurs
    # any number of amateurs less than 'chess_players_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

