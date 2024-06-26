darius_miles_driven = 679.0
julia_miles_driven = 998.0
total_miles_driven = darius_miles_driven + julia_miles_driven

if total_miles_driven == 1672.0:
    label = "entailment"
else:
    label = "contradiction"

print(label)
