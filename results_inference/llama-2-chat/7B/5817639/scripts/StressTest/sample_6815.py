students_with_cars_premise = 0.18
students_with_cars_hypothesis = 0.58

# the hypothesis talks about the percentage of students with cars at Morse, which is also referred to in the premise
if students_with_cars_premise <= students_with_cars_hypothesis:
    # check if the estimate of'students_with_cars_hypothesis' contradicts the number of students with cars in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students with cars, and any number greater than that estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
