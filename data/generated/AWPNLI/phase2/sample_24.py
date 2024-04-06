# Premise: Mike has 87.0 baseball cards and Sam bought 13.0 of Mike's baseball cards.
# Hypothesis: Mike has 74.0 baseball cards now.
# Golden Label: entailment

initial_cards_mike_premise = 87.0
bought_cards_sam_premise = 13.0
remaining_cards_mike_hypothesis = 74.0

# the hypothesis refers to the number of cards that Mike has after Sam bought some, which are also mentioned in the premise
# compute the remaining number of cards that Mike has in the premise
remaining_cards_mike_premise = initial_cards_mike_premise - bought_cards_sam_premise
if remaining_cards_mike_hypothesis != remaining_cards_mike_premise:
    # check if the number of cards in the hypothesis contradicts the number of cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

