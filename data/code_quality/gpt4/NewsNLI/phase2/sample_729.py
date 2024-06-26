rescued_people_premise = 282
rescued_people_hypothesis = 282

# The hypothesis mentions the total number of people rescued by two U.S. Navy ships
# But the premise only provides information about one ship rescuing 282 people
# There is no information about a second ship in the premise

# Check if the number of people rescued in the hypothesis contradicts the number of people rescued in the premise
if rescued_people_hypothesis != rescued_people_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
