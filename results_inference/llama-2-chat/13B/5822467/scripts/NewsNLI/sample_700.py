agents_premise = 200
locations_premise = 70
provinces_premise = 10
rescued_premise = 200

forces_hypothesis = 200
locations_hypothesis = 70
provinces_hypothesis = 10

# the hypothesis mentions the number of locations and provinces where the forces conducted raids, which are also mentioned in the premise
# however, the premise does not mention the number of agents or the number of people rescued, which are not referenced in the hypothesis
label = "neutral"

print(label)
