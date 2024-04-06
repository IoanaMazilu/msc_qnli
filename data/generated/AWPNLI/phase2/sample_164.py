# Premise: 14.0 birds were sitting in a tree and 21.0 more birds flew up to the tree.
# Hypothesis: 35.0 birds were there altogether in the tree.
# Golden Label: entailment

sitting_birds_premise = 14.0
flew_birds_premise = 21.0
total_birds_hypothesis = 35.0

# the hypothesis refers to the total number of birds, which are also mentioned in the premise
# compute the total number of birds in the premise
total_birds_premise = sitting_birds_premise + flew_birds_premise
if total_birds_hypothesis != total_birds_premise:
    # check if the total number of birds in the hypothesis contradicts the total number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

