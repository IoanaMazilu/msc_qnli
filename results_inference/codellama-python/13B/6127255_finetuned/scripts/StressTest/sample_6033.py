cat_dog_rabbit_owners_premise = 40
cat_dog_rabbit_owners_hypothesis = 70

# the hypothesis refers to the number of pet owners in San Durango mentioned in the premise
if cat_dog_rabbit_owners_premise >= cat_dog_rabbit_owners_hypothesis:
    # check if the number of pet owners in the premise contradicts the estimate of less than 'cat_dog_rabbit_owners_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
