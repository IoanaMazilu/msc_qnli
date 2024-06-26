heart_stones_premise = 48.0
bracelets_hypothesis = 8.0

# the hypothesis refers to the number of bracelets, which is also mentioned in the premise
# compute the total number of heart-shaped stones in the premise
total_heart_stones_premise = heart_stones_premise / bracelets_hypothesis

# check if the number of heart-shaped stones in the hypothesis contradicts the estimate from the premise
if total_heart_stones_hypothesis!= total_heart_stones_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
