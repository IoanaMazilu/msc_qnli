seniors_premise = 300
seniors_hypothesis = 400
car_owners_percentage_premise = 40
car_owners_percentage_hypothesis = 40

# the hypothesis refers to the number of seniors and their car ownership percentage mentioned in the premise
if seniors_premise!= seniors_hypothesis:
    # check if the number of seniors in the hypothesis contradicts the number of seniors reported in the premise
    label = "contradiction"
elif car_owners_percentage_premise!= car_owners_percentage_hypothesis:
    # check if the car ownership percentage in the hypothesis contradicts the car ownership percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
