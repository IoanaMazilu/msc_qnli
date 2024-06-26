boats_premise = 3.0
people_premise = 5.0
people_per_boat_hypothesis = 5.5

# the hypothesis refers to the number of people per boat, which is not mentioned in the premise
# compute the total number of people in the premise
total_people_premise = boats_premise * people_per_boat_hypothesis
if total_people_hypothesis!= total_people_premise:
    # check if the number of people from the hypothesis contradicts the number of people from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
