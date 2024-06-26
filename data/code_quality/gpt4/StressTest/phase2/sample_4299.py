tshirts_returned_premise = 1
tshirts_returned_hypothesis = 6

# the hypothesis refers to the number of t-shirts returned mentioned in the premise
if tshirts_returned_premise >= tshirts_returned_hypothesis:
    # check if the estimate of 'tshirts_returned_premise' contradicts the estimate in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
