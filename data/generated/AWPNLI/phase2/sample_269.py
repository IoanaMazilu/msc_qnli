# Premise: For the school bake sale Carol made 30.0 cupcakes, and she sold 9.0 of them and then made 28.0 more.
# Hypothesis: She would have 50.0 cupcakes.
# Golden Label: contradiction

made_cupcakes_premise = 30.0
sold_cupcakes_premise = 9.0
additional_cupcakes_premise = 28.0
total_cupcakes_hypothesis = 50.0

# the hypothesis refers to the number of cupcakes, which are also mentioned in the premise
# compute the total number of cupcakes in the premise
total_cupcakes_premise = made_cupcakes_premise - sold_cupcakes_premise + additional_cupcakes_premise
if total_cupcakes_hypothesis != total_cupcakes_premise:
    # check if the number of cupcakes in the hypothesis contradicts the number of cupcakes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

