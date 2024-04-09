shannon_stones_premise = 48.0
shannon_bracelets_hypothesis = 8.0

# compute the total number of heart-shaped stones needed for 8 bracelets
total_stones_needed = shannon_stones_premise * shannon_bracelets_hypothesis

if total_stones_needed > shannon_stones_premise:
    # check if the total number of heart-shaped stones needed in the hypothesis contradicts the number of stones brought in the premise
    label = "contradiction"
elif shannon_bracelets_hypothesis!= shannon_stones_premise / 8.0:
    # check if the number of bracelets that can be made with the stones in the hypothesis contradicts the number of bracelets and stones in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
