feathers_premise = 7.0
crowns_hypothesis = 934.0
total_feathers_hypothesis = 6533.0

# the hypothesis refers to the total number of feathers needed, which is also mentioned in the premise
# compute the total number of feathers needed according to the premise
total_feathers_premise = feathers_premise * crowns_hypothesis

if total_feathers_hypothesis!= total_feathers_premise:
    # check if the total number of feathers in the hypothesis contradicts the total number of feathers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(f"Label: {label}")
