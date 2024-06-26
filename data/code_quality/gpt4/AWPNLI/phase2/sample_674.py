initial_people_premise = 9
people_left_premise = 6
people_arrived_premise = 3
people_hypothesis = 18.0

# the hypothesis refers to the number of people in line, which is also mentioned in the premise
# compute the total number of people in the premise
total_people_premise = initial_people_premise - people_left_premise + people_arrived_premise
if people_hypothesis != total_people_premise:
    # check if the number of people in the hypothesis contradicts the number of people from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
