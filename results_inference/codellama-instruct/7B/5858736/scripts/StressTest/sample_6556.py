# Define variables for the numerical entities in the premise and hypothesis
last_year_england_france = 0
last_year_england_italy = 0
last_year_france_italy = 0
last_year_total = 0

# Extract all quantities as valid numbers
last_year_england_france = int(last_year_england_france)
last_year_england_italy = int(last_year_england_italy)
last_year_france_italy = int(last_year_france_italy)
last_year_total = int(last_year_total)

# Check if the hypothesis values contradict the premise
if last_year_england_france!= 0:
    label = "contradiction"
elif last_year_england_italy!= 0:
    label = "contradiction"
elif last_year_france_italy!= 0:
    label = "contradiction"
elif last_year_total!= 11:
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
