billion_premise = 1000000000
billion_hypothesis = 1000000000
trillion_premise = 1000000000000
trillion_hypothesis = 1000000000000

# the hypothesis mentions the values of billion and trillion, which are also mentioned in the premise
if billion_hypothesis!= billion_premise:
    # check if the value of billion in the hypothesis contradicts the value of billion in the premise
    label = "contradiction"
elif trillion_hypothesis!= trillion_premise:
    # check if the value of trillion from the hypothesis contradicts the value of trillion in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
