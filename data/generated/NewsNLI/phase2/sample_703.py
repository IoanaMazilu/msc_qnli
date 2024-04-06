# Premise: National Guard troops using'' high-profile'' trucks to wade through water evacuated 550 people from the Boulder County town of Lyons, CNN affiliate KUSA reported.
# Hypothesis: 231'' unaccounted for'' in Boulder County, 350 in Larimer County.
# Golden Label: neutral

evacuated_people_premise = 550
unaccounted_people_hypothesis = 231
unaccounted_people_larimer_hypothesis = 350

# The hypothesis mentions the number of unaccounted people in Boulder County and Larimer County, 
# while the premise mentions the number of people evacuated from Boulder County.
if evacuated_people_premise < unaccounted_people_hypothesis:
    # Check if the number of unaccounted people in Boulder County contradicts the number of people evacuated from Boulder County
    label = "contradiction"
else:
    # If the number of unaccounted people does not contradict the number of evacuated people, we infer neutrality
    label = "neutral"

print(label)

