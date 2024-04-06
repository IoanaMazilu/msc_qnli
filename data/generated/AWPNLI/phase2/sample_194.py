# Premise: There were 58.0 geese and 37.0 ducks in the marsh.
# Hypothesis: 95.0 birds were in the marsh.
# Golden Label: entailment

geese_premise = 58.0
ducks_premise = 37.0
total_birds_hypothesis = 95.0

# the hypothesis refers to the total number of birds, which are also mentioned in the premise
# compute the total number of birds in the premise
total_birds_premise = geese_premise + ducks_premise
if total_birds_hypothesis != total_birds_premise:
    # check if the number of birds in the hypothesis contradicts the number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
