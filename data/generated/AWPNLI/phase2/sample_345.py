# Premise: Shannon, Brenda’s neighbor, joined Brenda in making bracelets and she brought 48.0 heart-shaped stones and wanted to have 8.0 of this type of stone in each of the bracelet she makes.
# Hypothesis: Shannon can make 8.0 bracelets with heart-shaped stones.
# Golden Label: contradiction

stones_brought_premise = 48.0
stones_per_bracelet_premise = 8.0
bracelets_hypothesis = 8.0

# the hypothesis refers to the number of bracelets Shannon can make, which is also mentioned in the premise
# compute the number of bracelets Shannon can make from the premise
bracelets_premise = stones_brought_premise / stones_per_bracelet_premise
if bracelets_hypothesis != bracelets_premise:
    # check if the number of bracelets in the hypothesis contradicts the number of bracelets from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

