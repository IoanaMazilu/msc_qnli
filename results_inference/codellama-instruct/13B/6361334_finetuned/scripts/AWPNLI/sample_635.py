buses_premise = 8.0
students_premise = 45.0
students_per_bus_hypothesis = 3.1

# the hypothesis refers to the number of students in each bus, which are also mentioned in the premise
# compute the total number of students in the premise
total_students_premise = buses_premise * students_per_bus_hypothesis
if total_students_premise!= students_premise:
    # check if the number of students in the hypothesis contradicts the number of students from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
