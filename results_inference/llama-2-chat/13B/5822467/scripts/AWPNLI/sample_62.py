sally_baseball_cards_premise = 39.0
sally_baseball_cards_torn_premise = 9.0
sara_bought_baseball_cards_premise = 24.0
sally_baseball_cards_hypothesis = 15.0

# compute the total number of baseball cards Sally had before
total_baseball_cards_premise = sally_baseball_cards_premise - sally_baseball_cards_torn_premise

# check if the number of baseball cards Sally has now is consistent with the premise
if sally_baseball_cards_hypothesis >= total_baseball_cards_premise:
    # check if the number of baseball cards Sally has now contradicts the estimate of less than'sally_baseball_cards_torn_premise'
    label = "contradiction"
elif sally_baseball_cards_hypothesis!= total_baseball_cards_premise:
    # check if the number of baseball cards from the hypothesis contradicts the number of baseball cards in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
