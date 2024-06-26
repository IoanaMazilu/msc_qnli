initial_gum_premise = 54.0
received_gum_premise = 16.0
total_gum_hypothesis = 70.0

# the hypothesis refers to the total number of gum pieces, which are also mentioned in the premise
# compute the total number of gum pieces in the premise
total_gum_premise = initial_gum_premise + received_gum_premise
if total_gum_hypothesis!= total_gum_premise:
    # check if the total number of gum pieces in the hypothesis contradicts the total number of gum pieces from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
