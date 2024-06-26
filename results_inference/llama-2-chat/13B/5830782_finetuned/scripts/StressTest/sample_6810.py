seniors_premise = 300
seniors_hypothesis = 500
car_owners_premise = 0.5
car_owners_hypothesis = 0.5

# the hypothesis refers to the number of seniors and their car ownership percentage at Morse High School, as mentioned in the premise
if seniors_hypothesis <= seniors_premise:
    # check if the hypothesis estimate contradicts the exact number of seniors in the premise
    label = "contradiction"
elif car_owners_hypothesis!= car_owners_premise:
    # check if the car ownership percentage in the hypothesis contradicts the car ownership percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
