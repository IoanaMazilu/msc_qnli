each_purchased_premise = 20
each_purchased_hypothesis = 20

# the hypothesis talks about the number of items purchased each, referenced also in the premise
if each_purchased_hypothesis!= each_purchased_premise:
    # check if the number of items purchased each in the hypothesis contradicts the number of items purchased each reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
