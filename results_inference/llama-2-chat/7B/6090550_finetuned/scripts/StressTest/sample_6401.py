# Defining the variables
miami_airport_fraction = 1/2
kennedy_airport_fraction = 3/2
logan_airport_fraction = 4

# Defining the total number of passengers
total_passengers_premise = (miami_airport_fraction * logan_airport_fraction) + (kennedy_airport_fraction * logan_airport_fraction)
total_passengers_hypothesis = (miami_airport_fraction * logan_airport_fraction) + (kennedy_airport_fraction * logan_airport_fraction)

# Checking for entailment, contradiction or neutral
if total_passengers_premise!= total_passengers_hypothesis:
    # If the total number of passengers in the hypothesis contradicts the premise, then we have a contradiction
    label = "contradiction"
elif miami_airport_fraction!= 3/2 or kennedy_airport_fraction!= 4:
    # If any of the ratios in the hypothesis contradict the ratios in the premise, then we have a contradiction
    label = "contradiction"
else:
    # If the hypothesis values and ratios do not contradict the premise ones, then we have entailment
    label = "entailment"

print(label)
