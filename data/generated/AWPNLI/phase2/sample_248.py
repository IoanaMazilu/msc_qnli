# Premise: Lansing has 25.0 elementary schools and there are 247.0 students in each school.
# Hypothesis: 6175.0 elementary students are there altogether in Lansing.
# Golden Label: entailment

schools_premise = 25.0
students_per_school_premise = 247.0
total_students_hypothesis = 6175.0

# the hypothesis refers to the total number of students, which we can also compute from the premise
# compute the total number of students in the premise
total_students_premise = schools_premise * students_per_school_premise
if total_students_hypothesis != total_students_premise:
    # check if the total number of students in the hypothesis contradicts the total number of students from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

