baseball_cards_given_premise = 7
baseball_cards_given_hypothesis = 7

# the hypothesis refers to the number of baseball cards given to John mentioned in the premise
if baseball_cards_given_hypothesis >= baseball_cards_given_premise:
    # check if the hypothesis value contradicts the exact number 'baseball_cards_given_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
