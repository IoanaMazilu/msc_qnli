# Premise: Sarah signed 1/2 of the Christmas cards, and Richard signed 3/8 of them.
# Hypothesis: Sarah signed less than 3/2 of the Christmas cards, and Richard signed 3/8 of them.
# Golden Label: entailment

sarah_cards_signed_premise = 1/2
sarah_cards_signed_hypothesis = 3/2
richard_cards_signed_premise = 3/8
richard_cards_signed_hypothesis = 3/8

# the hypothesis refers to the number of Christmas cards Sarah and Richard signed, mentioned in the premise
if sarah_cards_signed_premise >= sarah_cards_signed_hypothesis:
    # check if the estimate of 'sarah_cards_signed_hypothesis' contradicts the number of cards Sarah signed in the premise
    label = "contradiction"
elif richard_cards_signed_hypothesis != richard_cards_signed_premise:
    # check if the number of cards Richard signed in the hypothesis contradicts the number of cards Richard signed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

