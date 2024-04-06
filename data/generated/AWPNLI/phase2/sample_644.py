# Premise: A pet supply store has 600.0 bags of dog food and they receive 327.0 bags of cat food.
# Hypothesis: There are 927.0 bags.
# Golden Label: entailment

dog_food_bags_premise = 600.0
cat_food_bags_premise = 327.0
total_bags_hypothesis = 927.0

# the hypothesis refers to the total number of bags, which are also mentioned in the premise
# compute the total number of bags in the premise
total_bags_premise = dog_food_bags_premise + cat_food_bags_premise
if total_bags_hypothesis != total_bags_premise:
    # check if the total number of bags in the hypothesis contradicts the total number of bags from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

