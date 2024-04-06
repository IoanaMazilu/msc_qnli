# Premise: A pet store had 13.0 siamese cats and 5.0 house cats and During a sale they sold 10.0 cats.
# Hypothesis: They has 12.0 cats left.
# Golden Label: contradiction

siamese_cats_premise = 13.0
house_cats_premise = 5.0
sold_cats_premise = 10.0
remaining_cats_hypothesis = 12.0

# the hypothesis refers to the number of cats, which are also mentioned in the premise
# compute the total number of cats in the premise
total_cats_premise = siamese_cats_premise + house_cats_premise
# compute the number of remaining cats in the premise
remaining_cats_premise = total_cats_premise - sold_cats_premise
if remaining_cats_hypothesis != remaining_cats_premise:
    # check if the number of remaining cats in the hypothesis contradicts the number of remaining cats from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

