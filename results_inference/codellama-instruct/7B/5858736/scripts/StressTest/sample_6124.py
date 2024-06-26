# Define variables for the numerical entities in the premise and hypothesis
people_iceland_premise = 35
people_norway_premise = 23
people_iceland_hypothesis = 35
people_norway_hypothesis = 23

# Define variables for the total number of people in the premise and hypothesis
total_people_premise = 20
total_people_hypothesis = 60

# Check if the hypothesis values contradict the premise values
if people_iceland_hypothesis!= people_iceland_premise or people_norway_hypothesis!= people_norway_premise:
    label = "contradiction"
elif people_iceland_hypothesis + people_norway_hypothesis!= total_people_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
