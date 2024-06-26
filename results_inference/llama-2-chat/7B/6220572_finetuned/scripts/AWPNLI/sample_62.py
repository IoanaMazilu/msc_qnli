cards_sally_premise = 39.0
cards_torn_premise = 9.0
cards_bought_premise = 24.0
cards_sally_hypothesis = 15.0

# the hypothesis refers to the number of baseball cards Sally has now, which is also mentioned in the premise
if cards_sally_hypothesis!= cards_sally_premise:
    # check if the number of baseball cards in the hypothesis contradicts the number of baseball cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
