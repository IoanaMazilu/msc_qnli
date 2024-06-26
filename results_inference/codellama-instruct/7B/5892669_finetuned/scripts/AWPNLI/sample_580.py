gum_premise = 54.0
gum_received = 16.0
gum_hypothesis = 70.0

# the hypothesis refers to the number of pieces of gum, which are also mentioned in the premise
# compute the total number of pieces of gum in the premise
total_gum_premise = gum_premise + gum_received
if gum_hypothesis!= total_gum_premise:
    # check if the number of pieces of gum in the hypothesis contradicts the number of pieces of gum from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
