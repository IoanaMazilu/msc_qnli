distance_run_by_each_sister_premise = 6
distance_run_by_each_sister_hypothesis = 8

# the hypothesis refers to the distance run by Sita and Geeta, which is also mentioned in the premise
if distance_run_by_each_sister_hypothesis < distance_run_by_each_sister_premise:
    # check if the hypothesis contradicts the distance run by each sister as stated in the premise
    label = "contradiction"
elif distance_run_by_each_sister_hypothesis > distance_run_by_each_sister_premise:
    # check if the hypothesis entails more distance run by each sister than stated in the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict or entail more than the premise ones, we can infer entailment
    label = "entailment"

print(label)
