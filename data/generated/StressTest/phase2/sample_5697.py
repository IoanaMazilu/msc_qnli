# Premise: Claire has a total of 80 pets consisting of gerbils and hamsters only.
# Hypothesis: Claire has a total of more than 30 pets consisting of gerbils and hamsters only.
# Golden Label: entailment

total_pets_premise = 80
total_pets_hypothesis = 30

# the hypothesis talks about the total number of pets Claire has, which is also referenced in the premise
if total_pets_premise < total_pets_hypothesis:
    # check if the number of pets in the hypothesis contradicts the number of pets in the premise
    label = "contradiction"
elif total_pets_hypothesis >= total_pets_premise:
    # check if the number of pets in the hypothesis is equal or greater than the number of pets in the premise
    label = "contradiction"
else:
    # if the number of pets in the hypothesis is less than the number in the premise, we can infer entailment
    label = "entailment"

print(label)

