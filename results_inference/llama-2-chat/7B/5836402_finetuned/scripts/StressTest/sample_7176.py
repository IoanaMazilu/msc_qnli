total_people_premise = 4800
ratio_premise = 2/4/6
total_people_hypothesis = 3800
ratio_hypothesis = 2/4/6

# the hypothesis refers to the total number of people and the ratio mentioned in the premise
if total_people_hypothesis < total_people_premise:
    # check if the estimate of 'total_people_hypothesis' contradicts the total number of people in the premise
    label = "contradiction"
elif ratio_hypothesis!= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
