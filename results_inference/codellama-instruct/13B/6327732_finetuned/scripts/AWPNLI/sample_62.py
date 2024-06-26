sally_baseball_cards_premise = 39.0
sally_torn_baseball_cards_premise = 9.0
sara_bought_baseball_cards_premise = 24.0
sally_baseball_cards_hypothesis = 15.0

# the hypothesis refers to the number of baseball cards, which are also mentioned in the premise
# compute the total number of baseball cards in the premise
total_baseball_cards_premise = sally_baseball_cards_premise + sally_torn_baseball_cards_premise
if sara_bought_baseball_cards_premise > total_baseball_cards_premise:
    # check if the number of baseball cards bought by Sara contradicts the number of baseball cards from the premise
    label = "contradiction"
elif sally_baseball_cards_hypothesis!= total_baseball_cards_premise:
    # check if the number of baseball cards in the hypothesis contradicts the number of baseball cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
