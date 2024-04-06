# Premise: One of those seven, Nicole Stott, will remain on the station as a flight engineer, while astronaut Timothy Kopra is to return home aboard the shuttle.
# Hypothesis: Discovery is scheduled to fly to international space station with a crew of seven.
# Golden Label: neutral

crew_premise = 7
crew_hypothesis = 7

# the hypothesis mentions the number of crew members, which is also referenced in the premise
# however, the hypothesis refers to a scheduled flight, which cannot be entailed from the premise
label = "neutral"

print(label)

