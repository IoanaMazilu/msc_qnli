# Premise: Martha has 3 dogs and 4 cats.
# Hypothesis: Martha has less than 6 dogs and 4 cats.
# Golden Label: entailment

dogs_martha_premise = 3
dogs_martha_hypothesis = 6
cats_martha_premise = 4
cats_martha_hypothesis = 4

# the hypothesis refers to the number of Martha's dogs and cats mentioned in the premise
if dogs_martha_premise >= dogs_martha_hypothesis:
    # check if the estimate of 'dogs_martha_hypothesis' contradicts the number of dogs Martha has in the premise
    label = "contradiction"
elif cats_martha_hypothesis != cats_martha_premise:
    # check if the number of cats Martha has in the hypothesis contradicts the number of cats Martha has in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

