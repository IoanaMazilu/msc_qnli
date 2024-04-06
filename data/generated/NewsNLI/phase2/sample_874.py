# Premise: Olsen, 24, had seen his share of war in two tours of Iraq as a Marine.
# Hypothesis: Scott Olsen returned from two tours of Iraq without injury.
# Golden Label: neutral

tours_premise = 2
tours_hypothesis = 2

# the hypothesis mentions the number of tours in Iraq, which is also mentioned in the premise
# however, the hypothesis refers to the status (without injury) of the person after the tours, which cannot be entailed from the premise
label = "neutral"

print(label)

