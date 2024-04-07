# Premise: In covering a distance of less than 50 km, Arun takes 2 hours more than Anil.
# Hypothesis: In covering a distance of 30 km, Arun takes 2 hours more than Anil.
# Golden Label: neutral

distance_covered_premise = 50
distance_covered_hypothesis = 30
time_difference = 2  # the time difference between Arun and Anil's travel times is constant across both sentences

# the hypothesis refers to the distance covered and time taken by Arun and Anil, which is also mentioned in the premise
if distance_covered_hypothesis >= distance_covered_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_covered_premise'
    label = "contradiction"
elif distance_covered_hypothesis < distance_covered_premise:
    # the premise gives only an estimate for the distance covered
    # any distance less than 'distance_covered_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

