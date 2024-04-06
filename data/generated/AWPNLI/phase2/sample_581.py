# Premise: Todd has 54.0 pieces of gum and Steve gave him 16.0 more pieces.
# Hypothesis: Todd has 73.0 pieces of gum now.
# Golden Label: contradiction

initial_gum_premise = 54.0
added_gum_premise = 16.0
total_gum_hypothesis = 73.0

# the hypothesis refers to the total number of pieces of gum, which is also mentioned in the premise
# compute the total number of pieces of gum in the premise
total_gum_premise = initial_gum_premise + added_gum_premise
if total_gum_hypothesis != total_gum_premise:
    # check if the total number of pieces of gum in the hypothesis contradicts the total number of pieces of gum from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

