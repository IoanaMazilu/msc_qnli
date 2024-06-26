seniors_premise = 300
seniors_hypothesis = 600
car_owners_percentage_premise = 50
car_owners_percentage_hypothesis = 50

# the hypothesis refers to the number of seniors and the percentage of car owners at Morse High School mentioned in the premise
if seniors_hypothesis <= seniors_premise:
    # check if the estimate of'seniors_hypothesis' contradicts the number of seniors in the premise
    label = "contradiction"
elif car_owners_percentage_hypothesis!= car_owners_percentage_premise:
    # check if the percentage of car owners in the hypothesis contradicts the percentage of car owners reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)