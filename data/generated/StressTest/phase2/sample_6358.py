# Premise: Since you're nice, you give John more than 2 baseball cards.
# Hypothesis: Since you're nice, you give John 5 baseball cards.
# Golden Label: neutral

baseball_cards_given_premise = 2
baseball_cards_given_hypothesis = 5

# the hypothesis mentions the number of baseball cards given to John, which is also referred to in the premise
if baseball_cards_given_hypothesis <= baseball_cards_given_premise:
    # check if the hypothesis value contradicts the premise of more than 'baseball_cards_given_premise'
    label = "contradiction"
else:
    # the premise provides only an estimate for the number of baseball cards given
    # any number of cards greater than 'baseball_cards_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

