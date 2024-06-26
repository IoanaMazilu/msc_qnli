neighbor_premise = "Shannon"
brenda_premise = "Brenda"
bracelets_premise = 48.0
stones_premise = 8.0

# the hypothesis refers to the number of bracelets made by the neighbor, which is also mentioned in the premise
# compute the total number of bracelets made by the neighbor and Brenda combined
total_bracelets_premise = bracelets_premise + stones_premise
if total_bracelets_premise!= 56.0:
    # check if the number of bracelets in the hypothesis contradicts the number of bracelets from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
