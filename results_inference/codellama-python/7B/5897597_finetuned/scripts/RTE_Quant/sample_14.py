people_lost_power_premise = 125000
people_killed_hypothesis = 125000

# the hypothesis talks about the number of people killed by a storm, which is not referenced in the premise (the premise only mentions people losing power)
# the hypothesis cannot be entailed from the premise, since the number of people killed is unknown.
label = "neutral"

print(label)