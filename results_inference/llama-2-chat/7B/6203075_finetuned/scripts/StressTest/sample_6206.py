each_purchased_premise = 20
each_purchased_hypothesis = 20

# the hypothesis refers to the number of each items purchased by Mohan from Ram, which is also mentioned in the premise
if each_purchased_hypothesis!= each_purchased_premise:
    # check if the number of each items in the hypothesis contradicts the number of each items in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
