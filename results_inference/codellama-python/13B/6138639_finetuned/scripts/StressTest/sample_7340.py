tshirts_returned_premise = 5
tshirts_returned_hypothesis = 4

# the hypothesis talks about the number of t-shirts returned to the retailer, referenced also in the premise
if tshirts_returned_hypothesis!= tshirts_returned_premise:
    # check if the number of t-shirts returned in the hypothesis contradicts the number of t-shirts returned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
