# Premise: A pet store had 13.0 siamese cats and 5.0 house cats and During a sale they sold 10.0 cats.
# Hypothesis: They has 8.0 cats left.
# Golden Label: entailment

siamese_cats_premise = 13.0
house_cats_premise = 5.0
sold_cats_premise = 10.0
left_cats_hypothesis = 8.0

# the hypothesis refers to the number of cats left, which are also mentioned in the premise
# compute the total number of cats in the premise
total_cats_premise = siamese_cats_premise + house_cats_premise
# compute the number of cats left after the sale from the premise
left_cats_premise = total_cats_premise - sold_cats_premise
if left_cats_hypothesis != left_cats_premise:
    # check if the number of cats left in the hypothesis contradicts the number of cats left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

