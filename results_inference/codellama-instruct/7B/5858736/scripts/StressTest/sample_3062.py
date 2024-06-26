# Define variables for the numerical entities in the premise and hypothesis
num_boys_premise = 6
num_girls_premise = 4
num_persons_committee_premise = 4

num_boys_hypothesis = 4
num_girls_hypothesis = 4
num_persons_committee_hypothesis = 4

# Check if the hypothesis values contradict the premise
if num_boys_hypothesis > num_boys_premise or num_girls_hypothesis > num_girls_premise:
    label = "contradiction"
elif num_persons_committee_hypothesis > num_persons_committee_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
