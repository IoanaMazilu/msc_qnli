mary_cards_premise = 18.0
promised_cards_premise = 26.0
bought_cards_premise = 40.0
left_cards_hypothesis = 32.0

# the hypothesis refers to the number of baseball cards left after giving Fred the promised cards, which are also mentioned in the premise
# compute the total number of cards Mary will have after buying and giving away cards
total_cards_premise = mary_cards_premise + bought_cards_premise - promised_cards_premise
if left_cards_hypothesis != total_cards_premise:
    # check if the number of cards left in the hypothesis contradicts the number of cards left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
