cars_premise = 3.0
people_per_car_premise = 63.0
total_people_hypothesis = 187.0

# the hypothesis refers to the total number of people going to the zoo, which can be calculated from the premise
# compute the total number of people in the premise
total_people_premise = cars_premise * people_per_car_premise
if total_people_hypothesis != total_people_premise:
    # check if the total number of people in the hypothesis contradicts the total number of people from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
