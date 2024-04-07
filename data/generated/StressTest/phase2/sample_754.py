# Premise: Martha has more than 1 dogs and 5 cats.
# Hypothesis: Martha has 5 dogs and 5 cats.
# Golden Label: neutral

dogs_martha_premise = 1
dogs_martha_hypothesis = 5
cats_martha_premise = 5
cats_martha_hypothesis = 5

# the hypothesis refers to the number of dogs and cats Martha has, as mentioned in the premise
if dogs_martha_hypothesis <= dogs_martha_premise:
    # check if the number of dogs in the hypothesis contradicts the estimate of more than 'dogs_martha_premise'
    label = "contradiction"
elif cats_martha_hypothesis != cats_martha_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of dogs
    # any number of dogs greater than 'dogs_martha_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

