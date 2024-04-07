# Premise: Since you're nice, you give John 5 baseball cards.
# Hypothesis: Since you're nice, you give John more than 5 baseball cards.
# Golden Label: contradiction

baseball_cards_premise = 5
baseball_cards_hypothesis = 5

# the hypothesis refers to the number of baseball cards given to John mentioned in the premise
if baseball_cards_hypothesis >= baseball_cards_premise:
    # check if the hypothesis estimate contradicts the specific number of baseball cards in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise's specific number of baseball cards, we can infer entailment
    label = "entailment"

print(label)

