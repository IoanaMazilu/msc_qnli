percentage_cars_premise = 50
percentage_cars_hypothesis = 20

# the hypothesis refers to the percentage of students with cars at Morse, which is also mentioned in the premise
if percentage_cars_hypothesis <= percentage_cars_premise:
    # check if the hypothesis value contradicts the estimate of less than 'percentage_cars_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of students with cars
    # any percentage of students with cars greater than 'percentage_cars_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
