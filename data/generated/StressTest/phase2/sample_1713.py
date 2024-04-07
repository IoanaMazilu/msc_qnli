# Premise: In a covering a distance of 30 km, Abhay takes 2 hours more than Sameer.
# Hypothesis: In a covering a distance of more than 10 km, Abhay takes 2 hours more than Sameer.
# Golden Label: entailment

distance_covered_premise = 30
distance_covered_hypothesis = 10
time_difference = 2

# the hypothesis refers to the distance covered and time taken by Abhay and Sameer mentioned in the premise
if distance_covered_hypothesis >= distance_covered_premise:
    # check if the estimate of 'distance_covered_hypothesis' contradicts the distance covered in the premise
    label = "contradiction"
elif time_difference != 2:
    # check if the time difference in the hypothesis contradicts the time difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

