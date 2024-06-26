premise_stones = 48.0
premise_bracelets = 8.0
hypothesis_bracelets = 8.0

# the hypothesis refers to the number of bracelets made by Shannon, which is also mentioned in the premise
# compute the total number of stones in the premise
total_stones_premise = premise_stones * premise_bracelets
if total_stones_premise!= hypothesis_bracelets:
    # check if the number of bracelets in the hypothesis contradicts the number of bracelets from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
