feathers_premise = 7.0
crowns_hypothesis = 934.0

# the hypothesis refers to the number of feathers needed for crowns, which is also mentioned in the premise
# compute the number of feathers in the premise
feathers_premise_premise = feathers_premise * (1 / 100)
if crowns_hypothesis!= feathers_premise_premise:
    # check if the number of feathers in the hypothesis contradicts the number of feathers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
