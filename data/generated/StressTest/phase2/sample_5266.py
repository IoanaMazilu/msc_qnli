# Premise: Since you're nice, you give John more than 1 baseball cards.
# Hypothesis: Since you're nice, you give John 2 baseball cards.
# Golden Label: neutral

baseball_cards_premise = 1
baseball_cards_hypothesis = 2

# the hypothesis talks about the number of baseball cards given to John, referenced also in the premise
if baseball_cards_hypothesis <= baseball_cards_premise:
    # check if the hypothesis value contradicts the estimate of more than 'baseball_cards_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of baseball cards
    # any number of baseball cards greater than 'baseball_cards_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

