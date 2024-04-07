# Premise: If 25% of all the students at Morse have cars, how many students are in the three lower grades?
# Hypothesis: If 85% of all the students at Morse have cars, how many students are in the three lower grades?
# Golden Label: contradiction

car_students_premise = 25
car_students_hypothesis = 85

# the hypothesis refers to the percentage of students who have cars, which is also mentioned in the premise
if car_students_hypothesis != car_students_premise:
    # check if the percentage of students who have cars in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

