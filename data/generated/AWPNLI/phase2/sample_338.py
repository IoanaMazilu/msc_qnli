# Premise: For the final act, the circus brought out dancing animals wearing crowns, and each crown is made with 7.0 different colored feathers.
# Hypothesis: 6538.0 feathers are needed for 934.0 crowns.
# Golden Label: entailment

feathers_per_crown_premise = 7.0
total_feathers_hypothesis = 6538.0
total_crowns_hypothesis = 934.0

# the hypothesis refers to the total number of feathers needed for crowns, which is also mentioned in the premise
# compute the total number of feathers needed in the premise
total_feathers_premise = feathers_per_crown_premise * total_crowns_hypothesis
if total_feathers_hypothesis != total_feathers_premise:
    # check if the total number of feathers in the hypothesis contradicts the total number of feathers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
