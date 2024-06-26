cards_jason_premise = 676.0
cards_bought_premise = 224.0
cards_jason_hypothesis = 452.0

# the hypothesis refers to the number of cards Jason has now, which is also mentioned in the premise
# compute the number of cards Jason has now according to the premise
cards_jason_now_premise = cards_jason_premise - cards_bought_premise
if cards_jason_hypothesis!= cards_jason_now_premise:
    # check if the number of cards in the hypothesis contradicts the number of cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
