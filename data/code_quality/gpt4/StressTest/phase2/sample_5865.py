dogs_premise = 5
dogs_hypothesis = 7
cats_premise = 6
cats_hypothesis = 6

# the hypothesis refers to the number of dogs and cats that Martha has, mentioned in the premise
if dogs_premise >= dogs_hypothesis:
    # check if the estimate of 'dogs_hypothesis' contradicts the number of dogs Martha has in the premise
    label = "contradiction"
elif cats_hypothesis != cats_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
