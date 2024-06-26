car_owners_premise = 20
car_owners_hypothesis = 50

# the hypothesis refers to the percentage of students with cars, mentioned also in the premise
if car_owners_hypothesis <= car_owners_premise:
    # check if the hypothesis percentage contradicts the percentage in the premise
    label = "contradiction"
elif car_owners_hypothesis > car_owners_premise:
    # if the hypothesis percentage is greater than the premise percentage, it means the premise cannot explicitly entail the hypothesis
    label = "neutral"

print(label)
