# Premise: Martha has 3 dogs and 4 cats.
# Hypothesis: Martha has less than 3 dogs and 4 cats.
# Golden Label: contradiction

dogs_premise = 3
cats_premise = 4
dogs_hypothesis = 3
cats_hypothesis = 4

# the hypothesis refers to the number of dogs and cats Martha has, as mentioned in the premise
if dogs_hypothesis >= dogs_premise:
    # check if the hypothesis value contradicts the premise of dogs being less than 'dogs_premise'
    label = "contradiction"
elif cats_hypothesis != cats_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

