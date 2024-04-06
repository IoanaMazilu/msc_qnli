# Premise: Sally had 39.0 baseball cards, and 9.0 were torn and Sara bought 24.0 of Sally's baseball cards.
# Hypothesis: Sally has 14.0 baseball cards now.
# Golden Label: contradiction

initial_cards_sally_premise = 39.0
torn_cards_premise = 9.0
bought_cards_sara_premise = 24.0
remaining_cards_sally_hypothesis = 14.0

# the hypothesis refers to the number of baseball cards Sally has now, which is also referenced in the premise
# find the remaining number of baseball cards with Sally from the premise 
remaining_cards_sally_premise = initial_cards_sally_premise - torn_cards_premise - bought_cards_sara_premise
if remaining_cards_sally_hypothesis != remaining_cards_sally_premise:
    # check if the remaining number of cards in the hypothesis contradicts the remaining number of cards in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)

