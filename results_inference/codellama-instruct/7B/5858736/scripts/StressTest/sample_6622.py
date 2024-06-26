# Define variables for the numerical entities in the premise and hypothesis
num_people = 7
min_committee_size = 1
max_committee_size = 5
at_least_one_jane_or_thomas = True

# Extract all quantities as valid numbers
num_possible_committees_premise = 0
num_possible_committees_hypothesis = 0

# Perform calculations
num_possible_committees_premise = binomial_coefficient(num_people, min_committee_size)
num_possible_committees_hypothesis = binomial_coefficient(num_people, max_committee_size)

# Check for entailment, contradiction, or neutrality
if num_possible_committees_hypothesis <= num_possible_committees_premise:
    label = "entailment"
elif at_least_one_jane_or_thomas:
    label = "neutral"
else:
    label = "contradiction"

print(label)
