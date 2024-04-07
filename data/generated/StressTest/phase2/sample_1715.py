# Premise: In a covering a distance of 30 km, Abhay takes 2 hours more than Sameer.
# Hypothesis: In a covering a distance of more than 30 km, Abhay takes 2 hours more than Sameer.
# Golden Label: contradiction

distance_covered_premise = 30
distance_covered_hypothesis = 30
extra_time_abhay_premise = 2
extra_time_abhay_hypothesis = 2

# the hypothesis refers to the distance covered and extra time taken by Abhay mentioned in the premise
if distance_covered_hypothesis <= distance_covered_premise:
    # check if the 'distance_covered_hypothesis' contradicts the premise
    label = "contradiction"
elif extra_time_abhay_hypothesis != extra_time_abhay_premise:
    # check if the extra time taken by Abhay in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality as the premise does not explicitly state the distance to be more than 30 km
    label = "neutral"

print(label)

