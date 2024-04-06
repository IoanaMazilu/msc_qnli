# Premise: There were 58.0 geese and 37.0 ducks in the marsh.
# Hypothesis: 98.0 birds were there in all.
# Golden Label: contradiction

geese_premise = 58.0
ducks_premise = 37.0
total_birds_hypothesis = 98.0

# the hypothesis refers to the total number of birds, which can be calculated from the premise
# compute the total number of birds in the premise
total_birds_premise = geese_premise + ducks_premise
if total_birds_hypothesis != total_birds_premise:
    # check if the total number of birds in the hypothesis contradicts the total number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment" 

print(label)

