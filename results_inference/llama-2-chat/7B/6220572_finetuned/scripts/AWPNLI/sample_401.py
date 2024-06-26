baseball_cards_mike_premise = 87.0
baseball_cards_given_premise = 13.0
baseball_cards_mike_hypothesis = 96.0

# the hypothesis talks about the number of baseball cards Mike has, which is also referenced in the premise
# compute the total number of baseball cards Mike has in the premise
total_baseball_cards_mike_premise = baseball_cards_mike_premise + baseball_cards_given_premise
if baseball_cards_mike_hypothesis!= total_baseball_cards_mike_premise:
    # check if the number of baseball cards from the hypothesis contradicts the number of baseball cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
