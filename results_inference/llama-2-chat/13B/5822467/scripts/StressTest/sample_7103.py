# Define variables with representative names for the numerical entities in both inputs
mile_premise = 240
mile_hypothesis = 140
hour_premise = 60
hour_hypothesis = 60

# Extract all quantities as valid numbers (integers or floats)
mile_premise_int = int(mile_premise)
mile_hypothesis_int = int(mile_hypothesis)
hour_premise_int = int(hour_premise)
hour_hypothesis_int = int(hour_hypothesis)

# Perform calculations if necessary
total_mile_premise = mile_premise_int + 120
total_mile_hypothesis = mile_hypothesis_int + 120
total_hour_premise = hour_premise_int * 2
total_hour_hypothesis = hour_hypothesis_int * 2

# Compare the variables and infer a label
if mile_hypothesis_int > mile_premise_int:
    # The hypothesis refers to a greater distance traveled than the premise, so we have a contradiction
    label = "contradiction"
elif mile_hypothesis_int == mile_premise_int:
    # The hypothesis refers to the same distance traveled as the premise, so we have neutrality
    label = "neutral"
else:
    # The hypothesis refers to a lesser distance traveled than the premise, so we have entailment
    label = "entailment"

print(label)
