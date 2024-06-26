sarah_cards_premise = 3/2
sarah_cards_hypothesis = 1/2
richard_cards_premise = 3/8
richard_cards_hypothesis = 3/8

# the hypothesis refers to the fraction of Christmas cards signed by Sarah and Richard as stated in the premise
if sarah_cards_hypothesis >= sarah_cards_premise:
    # check if the fraction of 'sarah_cards_hypothesis' contradicts the fraction of cards Sarah signed in the premise
    label = "contradiction"
elif richard_cards_hypothesis != richard_cards_premise:
    # check if the fraction of cards Richard signed in the hypothesis contradicts the fraction of cards Richard signed in the premise
    label = "contradiction"
elif sarah_cards_hypothesis < sarah_cards_premise and richard_cards_hypothesis == richard_cards_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
