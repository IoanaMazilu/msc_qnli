cards_premise = 210
cards_given_premise = 58
cards_hypothesis = 268

# the hypothesis refers to the total number of baseball cards, which is also mentioned in the premise
# compute the total number of baseball cards in the premise
total_cards_premise = cards_premise + cards_given_premise
if cards_hypothesis!= total_cards_premise:
    # check if the number of cards in the hypothesis contradicts the number of cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
