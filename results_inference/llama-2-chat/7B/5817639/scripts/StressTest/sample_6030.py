total_distance_premise = float(1/2) # 1/2 is the fraction of the total distance traveled by Maria so far
total_distance_hypothesis = float(less_than_8/2) # less than 8/2 is the fraction of the total distance to Maria's destination that she traveled

# the hypothesis refers to the remaining distance to Maria's destination
if total_distance_hypothesis <= total_distance_premise:
    # check if the estimate of 'total_distance_hypothesis' contradicts the remaining distance in the premise
    label = "contradiction"
elif total_distance_hypothesis > total_distance_premise:
    # check if the remaining distance in the hypothesis exceeds the remaining distance in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
