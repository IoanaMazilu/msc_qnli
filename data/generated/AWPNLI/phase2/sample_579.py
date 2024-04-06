# Premise: Marcus has 210.0 baseball cards and Carter gave him 58.0 more cards.
# Hypothesis: Marcus has 270.0 baseball cards now.
# Golden Label: contradiction

cards_initially_premise = 210.0
cards_received_premise = 58.0
total_cards_hypothesis = 270.0

# the hypothesis refers to the total number of baseball cards, which is also mentioned in the premise
# compute the total number of baseball cards Marcus has in the premise
total_cards_premise = cards_initially_premise + cards_received_premise
if total_cards_hypothesis != total_cards_premise:
    # check if the total number of cards in the hypothesis contradicts the total number of cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

