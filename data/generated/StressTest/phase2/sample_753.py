# Premise: Martha has 5 dogs and 5 cats.
# Hypothesis: Martha has more than 1 dogs and 5 cats.
# Golden Label: entailment

dogs_premise = 5
dogs_hypothesis = 1
cats_premise = 5
cats_hypothesis = 5

# the hypothesis refers to the number of dogs and cats that Martha has, mentioned in the premise
if dogs_premise <= dogs_hypothesis:
    # check if the estimate of 'dogs_hypothesis' contradicts the number of dogs in the premise
    label = "contradiction"
elif cats_hypothesis != cats_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

