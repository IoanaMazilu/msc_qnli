trip_home_premise = 1.5 # 1/2 hour longer than the trip to the beach
trip_beach_premise = 2 # 2 hours

# Convert the trip times to hours
trip_home_hypothesis = 7/2 # less than 7/2 hour longer than the trip to the beach

# Calculate the number of kilometers driven each way
km_home_premise = trip_home_premise * 60 # 60 minutes per hour
km_beach_premise = trip_beach_premise * 60

# Calculate the number of kilometers driven each way based on the hypothesis
km_home_hypothesis = trip_home_hypothesis * 60

# Compare the premise and hypothesis values
if km_home_premise <= km_home_hypothesis:
    label = "entailment"
elif km_home_hypothesis!= km_beach_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
