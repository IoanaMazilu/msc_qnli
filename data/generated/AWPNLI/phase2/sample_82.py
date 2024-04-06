# Premise: Mary had 33.0 Pokemon cards, and 6.0 were torn and Sam gave Mary 23.0 new Pokemon cards.
# Hypothesis: Mary has 56.0 Pokemon cards now.
# Golden Label: entailment

initial_cards_premise = 33.0
torn_cards_premise = 6.0
received_cards_premise = 23.0
total_cards_hypothesis = 56.0

# the hypothesis refers to the total number of cards Mary now has, which is also referenced in the premise
# compute the total number of cards Mary has in the premise
total_cards_premise = initial_cards_premise - torn_cards_premise + received_cards_premise
if total_cards_hypothesis != total_cards_premise:
    # check if the total number of cards in the hypothesis contradicts the total number of cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

