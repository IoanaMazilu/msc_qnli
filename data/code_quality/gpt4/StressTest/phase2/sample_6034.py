pet_owners_premise = 70
pet_owners_hypothesis = 40

# the hypothesis talks about the number of pet owners in a city, referenced also in the premise
if pet_owners_hypothesis >= pet_owners_premise:
    # check if the hypothesis value contradicts the estimate of less than 'pet_owners_premise'
    label = "contradiction"
elif pet_owners_hypothesis < pet_owners_premise:
    # if the hypothesis value is less than 'pet_owners_premise', it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
