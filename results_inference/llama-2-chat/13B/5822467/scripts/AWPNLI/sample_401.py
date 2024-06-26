mike_cards_premise = 87.0
sam_gave_premise = 13.0
total_cards_hypothesis = 96.0

# the hypothesis refers to the number of baseball cards, which are also mentioned in the premise
# compute the total number of baseball cards in the premise
total_cards_premise = mike_cards_premise + sam_gave_premise

if total_cards_hypothesis > total_cards_premise:
    # check if the number of baseball cards in the hypothesis entails the estimate of more than 'total_cards_premise'
    label = "entailment"
elif total_cards_hypothesis < total_cards_premise:
    # check if the number of baseball cards in the hypothesis contradicts the estimate of more than 'total_cards_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
