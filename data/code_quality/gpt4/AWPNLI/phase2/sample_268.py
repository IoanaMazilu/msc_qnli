made_cupcakes_premise = 30.0
sold_cupcakes_premise = 9.0
made_more_cupcakes_premise = 28.0
total_cupcakes_hypothesis = 49.0

# the hypothesis refers to the total number of cupcakes, which are also mentioned and calculated in the premise
# compute the total number of cupcakes in the premise
total_cupcakes_premise = made_cupcakes_premise - sold_cupcakes_premise + made_more_cupcakes_premise
if total_cupcakes_hypothesis != total_cupcakes_premise:
    # check if the total number of cupcakes in the hypothesis contradicts the total number of cupcakes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
