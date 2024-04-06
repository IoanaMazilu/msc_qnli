# Premise: Mary had 18.0 baseball cards and promised to give Fred 26.0 baseball cards, and Mary buys 40.0 baseball cards.
# Hypothesis: She will have 31.0 baseball cards left after she gives the promised cards to Fred.
# Golden Label: contradiction

cards_initial_premise = 18.0
cards_promised_premise = 26.0
cards_bought_premise = 40.0
cards_left_hypothesis = 31.0

# the hypothesis refers to the number of remaining cards after giving the promised cards, which are also mentioned in the premise
# compute the total number of cards in the premise
total_cards_premise = cards_initial_premise + cards_bought_premise
# compute the number of remaining cards after giving away promised cards
cards_left_premise = total_cards_premise - cards_promised_premise

if cards_left_hypothesis != cards_left_premise:
    # check if the number of remaining cards in the hypothesis contradicts the number of remaining cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

