# Define variables for the premise and hypothesis
num_people_premise = 5
num_people_hypothesis = 5
seat_premise = "middle"
seat_hypothesis = "middle"

# Check if the hypothesis is entailed from the premise
if num_people_hypothesis > num_people_premise:
    label = "entailment"
elif seat_hypothesis!= seat_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
