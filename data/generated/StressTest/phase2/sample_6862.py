# Premise: One hour after Matthew started waking from r to y, a distance of more than 35 km, Johnny started walking along the same road from y to r.
# Hypothesis: One hour after Matthew started waking from r to y, a distance of 45 km, Johnny started walking along the same road from y to r.
# Golden Label: neutral

distance_mathew_premise = 35
distance_mathew_hypothesis = 45

# the hypothesis refers to the distance Matthew walked, which is also mentioned in the premise
if distance_mathew_hypothesis <= distance_mathew_premise:
    # check if the distance in the hypothesis contradicts the premise's estimate of more than 'distance_mathew_premise'
    label = "contradiction"
else:
    # the premise only gives an estimate for the distance 
    # any distance greater than 'distance_mathew_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

