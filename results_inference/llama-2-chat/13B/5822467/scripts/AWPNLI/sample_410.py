jason_had_cards_premise = 9.0
jason_gave_cards_premise = 4.0
jason_has_cards_hypothesis = 5.0

# compute the difference between the number of cards Jason had and the number he gave away
cards_given_away_premise = jason_had_cards_premise - jason_gave_cards_premise

# check if the number of cards Jason has now is greater than or equal to the number of cards he gave away
if jason_has_cards_hypothesis >= cards_given_away_premise:
    # if the number of cards Jason has now is greater than or equal to the number of cards he gave away, we can infer entailment
    label = "entailment"
elif jason_has_cards_hypothesis < cards_given_away_premise:
    # if the number of cards Jason has now is less than the number of cards he gave away, we can infer contradiction
    label = "contradiction"
else:
    # if the number of cards Jason has now is equal to the number of cards he gave away, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
