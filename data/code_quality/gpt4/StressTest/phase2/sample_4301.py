tshirt_returned_premise = 1
tshirt_returned_hypothesis = 5

# the hypothesis refers to the number of t-shirts returned by Sanoop, which is also mentioned in the premise
if tshirt_returned_hypothesis != tshirt_returned_premise:
    # check if the number of t-shirts returned in the hypothesis contradicts the number of t-shirts returned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
