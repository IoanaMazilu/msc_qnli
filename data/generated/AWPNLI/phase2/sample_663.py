# Premise: A pet store had 13.0 siamese cats and 5.0 house cats and During a purchase, they added 10.0 cats.
# Hypothesis: They have 26.0 cats left.
# Golden Label: contradiction

siamese_cats_premise = 13.0
house_cats_premise = 5.0
added_cats_premise = 10.0
total_cats_hypothesis = 26.0

# the hypothesis refers to the total number of cats, which is related to the number of cats at the store in the premise
# compute the total number of cats in the premise
total_cats_premise = siamese_cats_premise + house_cats_premise + added_cats_premise
if total_cats_hypothesis != total_cats_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

