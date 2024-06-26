# Defining variables
miami_airport_fraction = 7/3
kennedy_airport_fraction = 1/3
logan_airport_fraction = 4

# Calculating the number of passengers that used Logan Airport
logan_airport_passengers_premise = (miami_airport_fraction * (miami_airport_fraction + kennedy_airport_fraction)) * logan_airport_fraction
logan_airport_passengers_hypothesis = (miami_airport_fraction * (miami_airport_fraction + kennedy_airport_fraction)) * logan_airport_fraction

# Checking if the hypothesis values contradict the premise ones
if logan_airport_passengers_hypothesis!= logan_airport_passengers_premise:
    label = "contradiction"
elif logan_airport_passengers_premise!= logan_airport_passengers_hypothesis:
    label = "contradiction"
else:
    label = "entailment"

print(label)
