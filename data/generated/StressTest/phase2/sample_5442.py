# Premise: Since you're nice, you give John 3 baseball cards.
# Hypothesis: Since you're nice, you give John less than 7 baseball cards.
# Golden Label: entailment

cards_given_premise = 3
cards_given_hypothesis = 7

# the hypothesis talks about the number of baseball cards given to John, referenced also in the premise
if cards_given_premise >= cards_given_hypothesis:
    # check if the number of cards given in the premise contradicts the estimate of less than 'cards_given_hypothesis'
    label = "contradiction"
elif cards_given_premise < cards_given_hypothesis:
    # check if the number of cards given in the premise is explicitly entailed by the hypothesis
    label = "entailment"
else:
    # the premise gives only an estimate for the number of cards
    # any number of cards less than 'cards_given_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

