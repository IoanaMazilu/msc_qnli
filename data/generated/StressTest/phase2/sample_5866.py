# Premise: Martha has less than 7 dogs and 6 cats.
# Hypothesis: Martha has 5 dogs and 6 cats.
# Golden Label: neutral

dogs_premise = 7
dogs_hypothesis = 5
cats_premise = 6
cats_hypothesis = 6

# the hypothesis refers to the number of dogs and cats Martha has, also mentioned in the premise
if dogs_hypothesis >= dogs_premise:
    # check if the hypothesis value contradicts the estimate of less than 'dogs_premise'
    label = "contradiction"
elif cats_hypothesis != cats_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of dogs
    # any number of dogs less than 'dogs_premise' is consistent with the premise
    label = "entailment"

print(label)

