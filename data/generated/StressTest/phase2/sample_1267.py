# Premise: Martha has less than 5 dogs and 4 cats.
# Hypothesis: Martha has 4 dogs and 4 cats.
# Golden Label: neutral

dogs_premise = 5
dogs_hypothesis = 4
cats_premise = 4
cats_hypothesis = 4

# the hypothesis refers to the number of dogs and cats Martha has, which is also mentioned in the premise
if dogs_hypothesis >= dogs_premise:
    # check if the number of dogs in the hypothesis contradicts the estimate of less than 'dogs_premise'
    label = "contradiction"
elif cats_hypothesis != cats_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

