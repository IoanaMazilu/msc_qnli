gum_initial_premise = 54.0
gum_received_premise = 16.0
total_gum_hypothesis = 70.0

# the hypothesis refers to the total number of gum pieces, which is also mentioned in the premise
# compute the total number of gum pieces in the premise
total_gum_premise = gum_initial_premise + gum_received_premise
if total_gum_hypothesis!= total_gum_premise:
    # check if the total number of gum pieces in the hypothesis contradicts the total number of gum pieces from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
