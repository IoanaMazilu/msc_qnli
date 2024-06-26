cards_mike_premise = 87.0
cards_mike_gift = 13.0
new_cards_mike_hypothesis = 96.0

# the hypothesis refers to the number of baseball cards Mike has, which is also mentioned in the premise
# compute the total number of cards Mike has in the premise
total_cards_mike_premise = cards_mike_premise + cards_mike_gift

if total_cards_mike_premise!= new_cards_mike_hypothesis:
    # check if the total number of cards in the premise contradicts the number of cards in the hypothesis
    label = "contradiction"
else:
    # if the total number of cards in the premise does not contradict the number of cards in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
