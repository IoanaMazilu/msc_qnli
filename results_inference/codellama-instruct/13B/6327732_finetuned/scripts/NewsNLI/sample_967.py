# define variables for the relevant information in the premise and hypothesis
premise_graduation = "The Citadel"
premise_former_officer = "U.S. Air Force"
hypothesis_name = "Tom Sponseller"
hypothesis_age = 61
hypothesis_association = "South Carolina Hospitality Association"

# check if the information in the hypothesis contradicts the information in the premise
if hypothesis_name!= premise_name:
    # if the name in the hypothesis does not match the name in the premise, we can infer contradiction
    label = "contradiction"
elif hypothesis_age!= premise_age:
    # if the age in the hypothesis does not match the age in the premise, we can infer contradiction
    label = "contradiction"
elif hypothesis_association!= premise_association:
    # if the association in the hypothesis does not match the association in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the information in the hypothesis does not contradict the information in the premise, we can infer neutral
    label = "neutral"

print(label)
