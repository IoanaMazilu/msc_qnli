initial_cards_sally_premise = 39.0
torn_cards_sally_premise = 9.0
bought_cards_sara_premise = 24.0
remaining_cards_sally_hypothesis = 15.0

# the hypothesis refers to the number of remaining baseball cards that Sally has, which is also mentioned in the premise
# compute the remaining number of baseball cards in the premise
remaining_cards_sally_premise = initial_cards_sally_premise - torn_cards_sally_premise - bought_cards_sara_premise
if remaining_cards_sally_hypothesis!= remaining_cards_sally_premise:
    # check if the number of remaining cards in the hypothesis contradicts the number of remaining cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
