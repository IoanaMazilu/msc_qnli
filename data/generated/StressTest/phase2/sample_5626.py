# Premise: In a deck of less than 72 cards, how many ways are there to select 13 Spade and 13 heart cards without repetition?
# Hypothesis: In a deck of 52 cards, how many ways are there to select 13 Spade and 13 heart cards without repetition?
# Golden Label: neutral

deck_size_premise = 72
deck_size_hypothesis = 52
spade_cards_premise = 13
spade_cards_hypothesis = 13
heart_cards_premise = 13
heart_cards_hypothesis = 13

# the hypothesis refers to the number of ways to select Spade and heart cards from a deck, also mentioned in the premise
if deck_size_hypothesis >= deck_size_premise:
    # check if the size of the deck in the hypothesis contradicts the premise
    label = "contradiction"
elif spade_cards_premise != spade_cards_hypothesis or heart_cards_premise != heart_cards_hypothesis:
    # check if the number of Spade or heart cards in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

