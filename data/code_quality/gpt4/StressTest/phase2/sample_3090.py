nos_premise = 20
nos_hypothesis = 50

# the hypothesis refers to the number of Nos. in a private company mentioned in the premise
if nos_premise >= nos_hypothesis:
    # check if the number of 'nos_premise' contradicts the estimate of less than 'nos_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
