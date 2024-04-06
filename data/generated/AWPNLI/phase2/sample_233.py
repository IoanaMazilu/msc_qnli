# Premise: A pet supply store has 600.0 bags of dog food and 327.0 bags of cat food.
# Hypothesis: 271.0 more bags of dog food are there than cat food.
# Golden Label: contradiction

dog_food_bags_premise = 600.0
cat_food_bags_premise = 327.0
more_dog_food_bags_hypothesis = 271.0

# the hypothesis refers to the number of dog food bags being more than the number of cat food bags, which are also mentioned in the premise
# compute the difference in the number of dog food and cat food bags in the premise
difference_bags_premise = dog_food_bags_premise - cat_food_bags_premise
if more_dog_food_bags_hypothesis != difference_bags_premise:
    # check if the difference in the number of bags in the hypothesis contradicts the difference in the number of bags from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

