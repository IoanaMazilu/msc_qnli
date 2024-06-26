tshirts_returned_premise = 4
tshirts_returned_hypothesis = 8

# the hypothesis refers to the number of t-shirts returned by Sanoop mentioned in the premise
if tshirts_returned_premise >= tshirts_returned_hypothesis:
    # check if the number of 'tshirts_returned_premise' contradicts the estimate of less than 'tshirts_returned_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
