pet_total_premise = 96
pet_total_hypothesis = 56

# the hypothesis talks about the total number of pets consisting of gerbils and hamsters, which is also referred to in the premise
if pet_total_hypothesis <= pet_total_premise:
    # check if the hypothesis value contradicts the estimate of 'pet_total_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the total number of pets, but the hypothesis value is greater than that estimate
    label = "entailment"

print(label)
