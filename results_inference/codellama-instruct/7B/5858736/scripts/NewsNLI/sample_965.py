gross_imprisonment_premise = 5
gross_imprisonment_hypothesis = 3

# the hypothesis mentions the number of Cuban spies imprisoned in the U.S., which is also mentioned in the premise
if gross_imprisonment_hypothesis!= gross_imprisonment_premise:
    # check if the number of Cuban spies imprisoned in the U.S. in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
