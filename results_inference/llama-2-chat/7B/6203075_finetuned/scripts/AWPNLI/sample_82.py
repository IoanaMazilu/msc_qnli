initial_cards_premise = 33.0
torn_cards_premise = 6.0
new_cards_hypothesis = 23.0
total_cards_hypothesis = initial_cards_premise + new_cards_hypothesis

# the hypothesis refers to the total number of Pokemon cards Mary has, which is also mentioned in the premise
# compute the total number of cards Mary has in the premise
total_cards_premise = initial_cards_premise + torn_cards_premise
if total_cards_hypothesis!= total_cards_premise:
    # check if the total number of cards in the hypothesis contradicts the total number of cards in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
