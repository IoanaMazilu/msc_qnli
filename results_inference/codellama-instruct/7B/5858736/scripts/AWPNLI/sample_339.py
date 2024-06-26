premise_crowns = 934.0
premise_feathers = 7.0
hypothesis_crowns = 6533.0
hypothesis_feathers = 934.0

# the hypothesis refers to the number of crowns and feathers, which are also mentioned in the premise
# compute the total number of feathers in the premise
total_feathers_premise = premise_crowns * premise_feathers
if hypothesis_feathers!= total_feathers_premise:
    # check if the number of feathers in the hypothesis contradicts the number of feathers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
