baseball_cards_premise = 210.0
cards_given_premise = 58.0

# compute the total number of baseball cards in the premise
total_cards_premise = baseball_cards_premise + cards_given_premise

baseball_cards_hypothesis = 268.0

# compare the total number of baseball cards in the premise and the hypothesis
if total_cards_premise > baseball_cards_hypothesis:
    # the hypothesis entails the premise
    label = "entailment"
elif total_cards_premise < baseball_cards_hypothesis:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis and premise have the same value, no inference can be made
    label = "neutral"

print(label)
