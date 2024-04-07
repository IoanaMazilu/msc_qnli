# Premise: Since you're nice, you give John 4 baseball cards.
# Hypothesis: Since you're nice, you give John less than 7 baseball cards.
# Golden Label: entailment

cards_given_premise = 4
cards_given_hypothesis = 7

# the hypothesis refers to the number of cards given to John mentioned in the premise
if cards_given_premise >= cards_given_hypothesis:
    # check if the number of 'cards_given_premise' contradicts the estimate of less than 'cards_given_hypothesis'
    label = "contradiction"
elif cards_given_premise != cards_given_hypothesis:
    # as the premise gives an exact number of cards, any number different from 'cards_given_premise' cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

