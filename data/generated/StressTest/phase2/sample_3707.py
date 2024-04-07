# Premise: Martha has 5 dogs and 4 cats.
# Hypothesis: Martha has 3 dogs and 4 cats.
# Golden Label: contradiction

dogs_premise = 5
cats_premise = 4
dogs_hypothesis = 3
cats_hypothesis = 4

# both the hypothesis and the premise refer to the number of dogs and cats Martha has
if dogs_hypothesis > dogs_premise:
    # check if the number of dogs in the hypothesis contradicts the number of dogs in the premise
    label = "contradiction"
elif cats_hypothesis != cats_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats in the premise
    label = "contradiction"
elif dogs_hypothesis < dogs_premise:
    # the premise clearly states that Martha has 5 dogs
    # hence, if the hypothesis states a lesser number of dogs, it cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict or deviate from the premise ones, we can infer entailment
    label = "entailment"

print(label)

