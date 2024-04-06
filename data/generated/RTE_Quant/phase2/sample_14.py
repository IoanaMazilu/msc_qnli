# Premise: The same storm has caused more than 125,000 people to lose power near St. Louis, Missouri and power officials say that they are '' still losing people,'' said Springfield's City Utilities spokesman, Ern DeCamp.
# Hypothesis: 125,000 were killed by a storm.
# Golden Label: neutral

people_lost_power_premise = 125000
people_killed_hypothesis = 125000

# the hypothesis talks about the number of people killed by the storm, which is not mentioned in the premise
# the premise only mentions the number of people who lost power due to the storm
# the hypothesis cannot be entailed from the premise, since the number of people killed is unknown.
label = "neutral"

print(label)

