# Premise: The 282 people were brought aboard the Bataan, and the Navy posted a YouTube video of the rescued people -- apparent African migrants -- looking tired or grateful as they stepped aboard the warship.
# Hypothesis: Two U.S. Navy ships rescue a total of 282 people.
# Golden Label: neutral

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

