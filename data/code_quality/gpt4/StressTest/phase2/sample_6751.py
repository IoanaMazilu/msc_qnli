pet_owners_premise = 70
pet_owners_hypothesis = 50

# the hypothesis is talking about the number of pet owners in San Durango city, which is also referenced in the premise
if pet_owners_hypothesis >= pet_owners_premise:
    # check if the hypothesis value contradicts the estimate of less than 'pet_owners_premise'
    label = "contradiction"
elif pet_owners_hypothesis < pet_owners_premise:
    # any number of pet owners less than 'pet_owners_premise' is consistent with the premise
    # as the exact number of pet owners is stated in the hypothesis, it can be explicitly entailed from the premise
    label = "entailment"

print(label)
