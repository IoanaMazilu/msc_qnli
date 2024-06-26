people_premise = float(3.0)
boats_premise = float(3.0)
people_per_boat_hypothesis = float(5.5)

# compare the number of people in each boat to the total number of people in the premise
if people_per_boat_hypothesis * boats_premise >= people_premise:
    # check if the average number of people in each boat contradicts the estimate of people in each boat from the premise
    label = "contradiction"
elif people_premise!= people_per_boat_hypothesis * boats_premise:
    # check if the number of people in each boat from the hypothesis contradicts the number of people in each boat from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
