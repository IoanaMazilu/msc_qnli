total_pencils_premise = 43.0 + 19.0 + 16.0
total_pencils_hypothesis = 81.0

# the hypothesis refers to the total number of pencils, which is also mentioned in the premise
# compute the total number of pencils in the premise
total_pencils_premise_computed = 43.0 + 19.0 + 16.0
if total_pencils_hypothesis!= total_pencils_premise_computed:
    # check if the total number of pencils in the hypothesis contradicts the total number of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are the same, we can infer entailment
    label = "entailment"

print(label)
