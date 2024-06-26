cat_dog_rabbit_owners_premise = 40
cat_dog_rabbit_owners_hypothesis = 70

# the hypothesis talks about the number of pet owners in San Durango, referenced also in the premise
if cat_dog_rabbit_owners_hypothesis >= cat_dog_rabbit_owners_premise:
    # check if the estimate of 'cat_dog_rabbit_owners_hypothesis' contradicts the number of pet owners in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pet owners
    # any number of pet owners greater than 'cat_dog_rabbit_owners_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
