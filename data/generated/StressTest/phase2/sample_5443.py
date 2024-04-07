# Premise: Since you're nice, you give John less than 7 baseball cards.
# Hypothesis: Since you're nice, you give John 3 baseball cards.
# Golden Label: neutral

baseball_cards_premise = 7
baseball_cards_hypothesis = 3

# the hypothesis refers to the number of baseball cards given to John, as in the premise
if baseball_cards_hypothesis >= baseball_cards_premise:
    # check if the number of baseball cards in the hypothesis contradicts the premise estimate of less than 'baseball_cards_premise' 
    label = "contradiction"
elif baseball_cards_hypothesis < baseball_cards_premise:
    # any number of cards less than 'baseball_cards_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise and can be inferred from it, we can infer entailment
    label = "entailment"

print(label)

