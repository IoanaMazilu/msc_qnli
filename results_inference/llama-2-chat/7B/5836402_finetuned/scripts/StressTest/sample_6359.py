cards_given_premise = 5
cards_given_hypothesis = 5

# the hypothesis refers to the number of baseball cards given to John, which is also mentioned in the premise
if cards_given_hypothesis <= cards_given_premise:
    # check if the hypothesis value contradicts the number of baseball cards given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
