baseball_cards_premise = 2
baseball_cards_hypothesis = 2

# the hypothesis talks about the number of baseball cards given to John, referenced also in the premise
if baseball_cards_hypothesis >= baseball_cards_premise:
    # check if the hypothesis value contradicts the exact number of 'baseball_cards_premise'
    label = "contradiction"
else:
    # if the hypothesis value is the same as the premise value, we can infer entailment
    label = "entailment"

print(label)
