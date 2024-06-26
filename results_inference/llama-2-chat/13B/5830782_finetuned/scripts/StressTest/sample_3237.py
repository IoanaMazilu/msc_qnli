car_owners_premise = 20
car_owners_hypothesis = 50

# the hypothesis refers to the percentage of students at Morse that own cars
if car_owners_hypothesis <= car_owners_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives a specific percentage of students that own cars
    # any percentage less than 'car_owners_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
