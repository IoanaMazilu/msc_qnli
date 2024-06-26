speed_premise = 3.0
time_premise = 6.0
distance_hypothesis = 18.0

# The hypothesis refers to the distance Charles travelled, which can be deduced from the premise
# compute total distance travelled in the premise
distance_premise = speed_premise * time_premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
