# Premise: In a covering a distance of 30 km, Abhay takes 2 hours more than Sameer.
# Hypothesis: In a covering a distance of less than 50 km, Abhay takes 2 hours more than Sameer.
# Golden Label: entailment

distance_covered_premise = 30
distance_covered_hypothesis = 50
time_difference = 2

# the hypothesis talks about the distance covered and the time it takes for Abhay and Sameer, referenced also in the premise
if distance_covered_hypothesis <= distance_covered_premise:
    # check if the hypothesis value contradicts the distance covered in the premise
    label = "contradiction"
elif distance_covered_hypothesis > distance_covered_premise:
    # the hypothesis value for distance is more than what is mentioned in the premise
    # thus, we can't explicitly infer the hypothesis from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

