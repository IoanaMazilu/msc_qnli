seniors_premise = 300
seniors_hypothesis = 800
car_owners_percentage = 40

# the hypothesis refers to the number of seniors at Morse High School and the percentage of them owning cars
if seniors_premise > seniors_hypothesis:
    # check if the number of seniors specified in the premise contradicts the number in the hypothesis
    label = "contradiction"
elif car_owners_percentage != 40:
    # check if the percentage of car owners in the premise contradicts the one in the hypothesis
    label = "contradiction"
else:
    # if the number of seniors and the percentage of car owners do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
