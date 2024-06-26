seniors_premise = 300
seniors_hypothesis = 800
car_owners_premise = 40
car_owners_hypothesis = 40

# the hypothesis refers to the number of seniors and the percentage of car owners at Morse High School mentioned in the premise
if seniors_premise >= seniors_hypothesis:
    # check if the estimate of'seniors_hypothesis' contradicts the number of seniors in the premise
    label = "contradiction"
elif car_owners_hypothesis!= car_owners_premise:
    # check if the percentage of car owners in the hypothesis contradicts the percentage of car owners reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
