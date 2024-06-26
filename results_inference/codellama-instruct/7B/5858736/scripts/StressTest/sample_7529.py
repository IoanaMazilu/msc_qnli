# Define variables for the number of boys and girls in the group
num_boys_premise = 6
num_girls_premise = 4
num_boys_hypothesis = 3
num_girls_hypothesis = 4

# Define variables for the number of persons in the committee
num_persons_committee_premise = 4
num_persons_committee_hypothesis = 4

# Check if the number of boys and girls in the hypothesis is consistent with the premise
if num_boys_hypothesis <= num_boys_premise and num_girls_hypothesis <= num_girls_premise:
    # Check if the number of persons in the committee in the hypothesis is consistent with the premise
    if num_persons_committee_hypothesis <= num_persons_committee_premise:
        # The hypothesis is entailed from the premise
        label = "entailment"
    else:
        # The hypothesis contradicts the premise
        label = "contradiction"
else:
    # The hypothesis contradicts the premise
    label = "contradiction"

print(label)
