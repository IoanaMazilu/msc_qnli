seniors_premise = 600
seniors_hypothesis = 300
car_owners_percentage_premise = car_owners_percentage_hypothesis = 50

# the hypothesis refers to the number of seniors and the percentage of car owners at Morse High School mentioned in the premise
if seniors_hypothesis >= seniors_premise:
    # check if the hypothesis value contradicts the estimate of less than 'seniors_premise'
    label = "contradiction"
elif car_owners_percentage_hypothesis != car_owners_percentage_premise:
    # check if the percentage of car owners in the hypothesis contradicts the percentage of car owners reported in the premise
    label = "contradiction"
else:
    # any number of seniors less than 'seniors_premise' is consistent with the premise
    # also, the percentage of car owners in the hypothesis is equal to the one in the premise
    # hence, we cannot explicitly entail the hypothesis from the premise, but there is no contradiction either
    label = "neutral"

print(label)
