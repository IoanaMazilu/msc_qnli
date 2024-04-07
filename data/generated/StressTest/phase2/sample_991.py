# Premise: If less than 35% of all the students at Morse have cars, how many students are in the three lower grades?
# Hypothesis: If 15% of all the students at Morse have cars, how many students are in the three lower grades?
# Golden Label: neutral

car_students_premise = 35
car_students_hypothesis = 15

# the hypothesis refers to the percentage of students with cars mentioned in the premise
if car_students_hypothesis >= car_students_premise:
    # check if the 'car_students_hypothesis' contradicts the number of car students in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

