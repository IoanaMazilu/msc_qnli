# Define variables for numerical entities in the premise and hypothesis
bean_counts_premise = {
    'Aaron': 5,
    'Bianca': 7,
    'Callie': 8,
    'Dante': 13
}

bean_counts_hypothesis = {
    'Aaron': less_than_7,
    'Bianca': 7,
    'Callie': 8,
    'Dante': 13
}

# Extract all quantities as valid numbers (integers or floats)
for name, count in bean_counts_premise.items():
    if not isinstance(count, int) and not isinstance(count, float):
        raise ValueError(f"{name} should be an integer or float, not {type(count)}")

for name, count in bean_counts_hypothesis.items():
    if not isinstance(count, int) and not isinstance(count, float):
        raise ValueError(f"{name} should be an integer or float, not {type(count)}")

# Perform calculations and comparisons
less_than_7 = int(bean_counts_hypothesis['Aaron'])

if bean_counts_premise['Aaron'] > less_than_7:
    label = "contradiction"
elif bean_counts_premise['Bianca']!= bean_counts_hypothesis['Bianca']:
    label = "contradiction"
elif bean_counts_premise['Callie']!= bean_counts_hypothesis['Callie']:
    label = "neutral"
else:
    label = "entailment"

print(label)
