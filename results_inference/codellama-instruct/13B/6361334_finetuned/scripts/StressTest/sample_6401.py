# define variables for the numerical entities in the premise
miami_airport_passengers = 1/2 * kennedy_airport_passengers
logan_airport_passengers = 4 * logan_airport_passengers

# define variables for the numerical entities in the hypothesis
miami_airport_passengers_hypothesis = 3/2 * kennedy_airport_passengers_hypothesis
logan_airport_passengers_hypothesis = 4 * logan_airport_passengers_hypothesis

# check if the hypothesis values contradict the premise values
if miami_airport_passengers_hypothesis!= miami_airport_passengers:
    label = "contradiction"
elif logan_airport_passengers_hypothesis!= logan_airport_passengers:
    label = "contradiction"
else:
    label = "neutral"

print(label)
