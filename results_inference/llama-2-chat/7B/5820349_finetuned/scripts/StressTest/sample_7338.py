tshirts_returned_premise = 5
tshirts_returned_hypothesis = 4

# the hypothesis refers to the number of t-shirts returned by Sanoop, mentioned in the premise
if tshirts_returned_premise <= tshirts_returned_hypothesis:
    # check if the estimate of 'tshirts_returned_hypothesis' contradicts the number of t-shirts returned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
