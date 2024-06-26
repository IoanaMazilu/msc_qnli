baseball_cards_premise = 39.0
torn_cards_premise = 9.0
new_cards_hypothesis = 24.0

# the hypothesis talks about the number of baseball cards Sally has, which is also mentioned in the premise
# compute the total number of baseball cards Sally had before the purchase
total_baseball_cards_premise = baseball_cards_premise + torn_cards_premise
if total_baseball_cards_hypothesis!= total_baseball_cards_premise:
    # check if the number of baseball cards in the hypothesis contradicts the number of baseball cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
