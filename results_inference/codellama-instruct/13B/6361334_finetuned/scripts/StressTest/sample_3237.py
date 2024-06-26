percentage_cars_premise = 20
percentage_cars_hypothesis = 50

# the hypothesis refers to the percentage of students with cars at Morse, mentioned in the premise
if percentage_cars_hypothesis >= percentage_cars_premise:
    # check if the hypothesis value contradicts the percentage of students with cars in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of students with cars
    # any percentage of students with cars less than 'percentage_cars_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
