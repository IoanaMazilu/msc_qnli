billion_premise = 1000000000
billion_hypothesis = 1000000000
trillion_premise = 1000000000000
trillion_hypothesis = 1000000000000

if billion_hypothesis!= billion_premise:
    # check if the hypothesis value for billion contradicts the premise value
    label = "contradiction"
elif trillion_hypothesis!= trillion_premise:
    # check if the hypothesis value for trillion contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
