heart_stones_premise = 48.0
heart_stones_per_bracelet_premise = 8.0
bracelets_hypothesis = 8.0

# the hypothesis refers to the number of bracelets Shannon can make, which is also mentioned in the premise
# compute the total number of bracelets Shannon can make according to the premise
bracelets_premise = heart_stones_premise / heart_stones_per_bracelet_premise
if bracelets_hypothesis!= bracelets_premise:
    # check if the number of bracelets in the hypothesis contradicts the number of bracelets from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
