pet_owners_premise = 70
pet_owners_hypothesis = 50

# the hypothesis talks about the number of pet owners in San Durango, referenced also in the premise
if pet_owners_hypothesis >= pet_owners_premise:
    # check if the hypothesis value contradicts the estimate of less than 'pet_owners_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pet owners
    # any number of pet owners less than 'pet_owners_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
