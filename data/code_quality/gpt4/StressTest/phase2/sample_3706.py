dogs_premise = 8
dogs_hypothesis = 5
cats_premise = 4
cats_hypothesis = 4

# the hypothesis refers to the number of Martha's dogs and cats mentioned in the premise
if dogs_hypothesis >= dogs_premise:
    # check if the hypothesis value contradicts the estimate of less than 'dogs_premise'
    label = "contradiction"
elif cats_hypothesis != cats_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats reported in the premise
    label = "contradiction"
else:
    # the premise provides an estimate for the number of dogs and an exact number for the cats
    # any number of dogs less than 'dogs_premise' and number of cats equal to 'cats_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
