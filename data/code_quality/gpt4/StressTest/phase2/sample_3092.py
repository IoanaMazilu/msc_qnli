nos_premise = 20
nos_hypothesis = 20

# the hypothesis refers to an estimate of the number of Nos. in a private company, which is also mentioned in the premise
if nos_hypothesis >= nos_premise:
    # check if the hypothesis estimate contradicts the 'nos_premise'
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the number of Nos. in the premise, we can infer entailment
    label = "entailment"

print(label)
