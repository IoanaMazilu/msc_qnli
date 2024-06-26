cards_initial_premise = 39.0
cards_torn_premise = 9.0
cards_bought_premise = 24.0
cards_hypothesis = 15.0

# the hypothesis refers to the number of baseball cards, which are also mentioned in the premise
# compute the total number of baseball cards in the premise
total_cards_premise = cards_initial_premise - cards_torn_premise + cards_bought_premise
if cards_hypothesis!= total_cards_premise:
    # check if the number of baseball cards in the hypothesis contradicts the number of cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
