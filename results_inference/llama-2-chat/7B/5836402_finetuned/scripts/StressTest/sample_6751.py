cat_dog_rabbit_owners_premise = 70
cat_dog_rabbit_owners_hypothesis = 50

# the hypothesis refers to the number of cat, dog and rabbit owners in San Durango, mentioned in the premise
if cat_dog_rabbit_owners_hypothesis >= cat_dog_rabbit_owners_premise:
    # check if the number of owners in the hypothesis contradicts the estimate of less than 'cat_dog_rabbit_owners_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of owners
    # any number of owners less than 'cat_dog_rabbit_owners_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
