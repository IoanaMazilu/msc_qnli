# Premise: Martha has less than 6 dogs and 4 cats.
# Hypothesis: Martha has 3 dogs and 4 cats.
# Golden Label: neutral

dogs_premise = 6
dogs_hypothesis = 3
cats_premise = 4
cats_hypothesis = 4

# the hypothesis talks about the number of dogs and cats Martha has, referenced also in the premise
if dogs_hypothesis >= dogs_premise:
    # check if the hypothesis value contradicts the estimate of less than 'dogs_premise'
    label = "contradiction"
elif cats_hypothesis != cats_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of dogs
    # the number of dogs in the hypothesis is less than 'dogs_premise' and the number of cats matches the premise, so we can infer entailment
    label = "entailment"

print(label)

