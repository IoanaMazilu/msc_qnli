car_owners_percentage_premise = 50
car_owners_percentage_hypothesis = 20

# the hypothesis refers to the percentage of students owning cars at Morse, which is also mentioned in the premise
if car_owners_percentage_hypothesis >= car_owners_percentage_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'car_owners_percentage_premise'
    label = "contradiction"
elif car_owners_percentage_hypothesis < car_owners_percentage_premise:
    # the premise gives only an estimate for the percentage of students owning cars
    # any percentage less than 'car_owners_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
