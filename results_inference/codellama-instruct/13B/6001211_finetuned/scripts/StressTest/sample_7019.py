seniors_premise = 300
seniors_hypothesis = 400
car_owners_premise = 0.4 * seniors_premise
car_owners_hypothesis = 0.4 * seniors_hypothesis

# the hypothesis refers to the number of seniors and car owners at Morse High School mentioned in the premise
if seniors_hypothesis!= seniors_premise:
    # check if the number of seniors in the hypothesis contradicts the number of seniors reported in the premise
    label = "contradiction"
elif car_owners_hypothesis!= car_owners_premise:
    # check if the percentage of car owners in the hypothesis contradicts the percentage of car owners reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
