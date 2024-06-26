initial_people_premise = 9
left_people_premise = 6
joined_people_premise = 3
total_people_hypothesis = 16.0

# the hypothesis refers to the number of people in line, which are also mentioned in the premise
# compute the total number of people in line at some point in the premise
total_people_premise = initial_people_premise + joined_people_premise
if total_people_hypothesis != total_people_premise:
    # check if the total number of people in the hypothesis contradicts the total number of people from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
