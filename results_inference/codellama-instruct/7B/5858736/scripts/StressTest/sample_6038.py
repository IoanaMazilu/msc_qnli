# Define variables for the numerical entities in the premise and hypothesis
num_members_premise = 59
min_clubs_premise = 1
max_clubs_premise = 3
num_members_hypothesis = 59
min_clubs_hypothesis = 1
max_clubs_hypothesis = 3

# Check if the hypothesis values and estimates do not contradict the premise ones
if num_members_hypothesis <= num_members_premise and min_clubs_hypothesis <= min_clubs_premise and max_clubs_hypothesis <= max_clubs_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
