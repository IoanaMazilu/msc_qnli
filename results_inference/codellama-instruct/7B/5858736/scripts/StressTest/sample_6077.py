# Define variables for the time it takes to rake a lawn
time_rake_lawn_john = 30
time_rake_lawn_todd = 60

# Check if the hypothesis values contradict the premise
if time_rake_lawn_john > time_rake_lawn_premise:
    label = "contradiction"
elif time_rake_lawn_todd!= time_rake_lawn_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
