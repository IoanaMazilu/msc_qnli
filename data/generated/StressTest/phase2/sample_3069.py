# Premise: 90 students represent x percent of the boys at Jones Elementary School.
# Hypothesis: more than 60 students represent x percent of the boys at Jones Elementary School.
# Golden Label: entailment

students_premise = 90
students_hypothesis = 60

# the hypothesis talks about the number of students representing x percent of boys, referenced also in the premise
if students_hypothesis >= students_premise:
    # check if the hypothesis value contradicts the value mentioned in the premise
    label = "contradiction"
elif students_hypothesis < students_premise:
    # since the premise clearly states the number of students that represent x percent of boys
    # and the hypothesis infers a number less than that, we can infer entailment
    label = "entailment"

print(label)

