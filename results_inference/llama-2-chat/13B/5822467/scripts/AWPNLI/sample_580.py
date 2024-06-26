gum_premise = 54.0
gum_given_premise = 16.0
total_gum_hypothesis = 70.0

# compute the total number of gum in the premise
total_gum_premise = gum_premise + gum_given_premise

if total_gum_hypothesis > total_gum_premise:
    # check if the number of gum in the hypothesis contradicts the number of gum from the premise
    label = "contradiction"
elif total_gum_hypothesis < total_gum_premise:
    # check if the number of gum in the hypothesis is less than the estimate in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
