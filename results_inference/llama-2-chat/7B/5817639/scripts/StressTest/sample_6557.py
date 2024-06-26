# Variables for premise and hypothesis
last_year_england_france_premise = 0
last_year_england_italy_premise = 6
last_year_france_italy_premise = 11

# Define variables for hypothesis
no_members_england_france_hypothesis = 0
no_members_england_italy_hypothesis = 2
no_members_france_italy_hypothesis = 11

# Check for entailment, contradiction, or neutrality
if no_members_england_france_hypothesis <= last_year_england_france_premise:
    label = "contradiction"
elif no_members_england_italy_hypothesis!= no_members_england_italy_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
