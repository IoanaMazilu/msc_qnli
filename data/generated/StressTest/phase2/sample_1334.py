# Premise: In covering a distance of 30 km, Arun takes 2 hours more than Anil.
# Hypothesis: In covering a distance of less than 30 km, Arun takes 2 hours more than Anil.
# Golden Label: contradiction

distance_covered_premise = 30
distance_covered_hypothesis = 30
time_difference = 2

# the hypothesis refers to the distance covered and the time taken by Arun and Anil, mentioned in the premise
if distance_covered_hypothesis >= distance_covered_premise:
    # check if the 'distance_covered_hypothesis' contradicts the premise statement of less than 'distance_covered_premise'
    label = "contradiction"
elif time_difference != 2:
    # check if the time difference in the hypothesis contradicts the time difference mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

