# Premise: There are 4 chess amateurs playing in Villa's chess club tournament.
# Hypothesis: There are less than 8 chess amateurs playing in Villa's chess club tournament.
# Golden Label: entailment

chess_players_premise = 4
chess_players_hypothesis = 8

# the hypothesis talks about the number of chess players in a tournament, referenced also in the premise
if chess_players_premise >= chess_players_hypothesis:
    # check if the number of chess players in the premise contradicts the estimate of less than 'chess_players_hypothesis'
    label = "contradiction"
elif chess_players_premise < chess_players_hypothesis:
    # if the number of chess players in the premise is less than 'chess_players_hypothesis', we can infer entailment
    label = "entailment"

print(label)

