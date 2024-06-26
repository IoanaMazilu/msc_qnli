dogs_premise = 2
dogs_hypothesis = 6
cats_premise = 4
cats_hypothesis = 4

# the hypothesis talks about the number of dogs and cats Martha has, referenced also in the premise
if dogs_hypothesis <= dogs_premise:
    # check if the hypothesis value contradicts the estimate of more than 'dogs_premise'
    label = "contradiction"
elif cats_hypothesis != cats_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of dogs
    # any number of dogs greater than 'dogs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
