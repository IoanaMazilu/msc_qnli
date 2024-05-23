seniors_premise = 300
seniors_hypothesis = 300
car_owners_percentage_premise = 50
car_owners_percentage_hypothesis = 50

# the hypothesis talks about the number of seniors and the percentage of car owners at Morse High School, referenced also in the premise
if seniors_hypothesis <= seniors_premise:
    # check if the hypothesis value contradicts the exact number of'seniors_premise'
    label = "contradiction"
elif car_owners_percentage_hypothesis!= car_owners_percentage_premise:
    # check if the percentage of car owners in the hypothesis contradicts the percentage of car owners reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)