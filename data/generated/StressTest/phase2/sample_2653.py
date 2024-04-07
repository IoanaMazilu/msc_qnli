# Premise: In a covering a distance of less than 50 km, Abhay takes 2 hours more than Sameer.
# Hypothesis: In a covering a distance of 30 km, Abhay takes 2 hours more than Sameer.
# Golden Label: neutral

distance_covered_premise = 50
distance_covered_hypothesis = 30
extra_time_taken_by_abhay = 2

# the hypothesis refers to the distance covered and time taken by Abhay and Sameer mentioned in the premise
if distance_covered_hypothesis >= distance_covered_premise:
    # check if the distance covered in the hypothesis contradicts the estimate of less than 'distance_covered_premise'
    label = "contradiction"
elif extra_time_taken_by_abhay != 2:
    # check if the extra time taken by Abhay in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

