cats_dogs_rabbits_premise = 70
cats_dogs_rabbits_hypothesis = 50

# the hypothesis talks about the number of pet owners in San Durango, referenced also in the premise
if cats_dogs_rabbits_hypothesis >= cats_dogs_rabbits_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cats_dogs_rabbits_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pet owners
    # any number of pet owners less than 'cats_dogs_rabbits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
