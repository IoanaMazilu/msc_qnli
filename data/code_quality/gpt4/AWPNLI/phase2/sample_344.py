stones_brought_premise = 48.0
stones_per_bracelet_premise = 8.0
bracelets_hypothesis = 6.0

# the hypothesis refers to the number of bracelets Shannon can make, which is based on the number of stones she brought and how many she wants in each bracelet
# compute the maximum number of bracelets Shannon can make in the premise
bracelets_premise = stones_brought_premise / stones_per_bracelet_premise
if bracelets_hypothesis != bracelets_premise:
    # check if the number of bracelets in the hypothesis contradicts the number of bracelets Shannon can make from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
