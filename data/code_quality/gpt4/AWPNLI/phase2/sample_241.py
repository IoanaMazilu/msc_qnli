cereal_in_box_premise = 18.0
serving_size_premise = 2.0
number_of_servings_hypothesis = 8.0

# the hypothesis refers to the number of servings, which are also mentioned in the premise
# compute the total number of servings in the premise
total_servings_premise = cereal_in_box_premise / serving_size_premise
if number_of_servings_hypothesis != total_servings_premise:
    # check if the number of servings in the hypothesis contradicts the number of servings from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
