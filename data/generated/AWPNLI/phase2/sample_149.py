# Premise: There were 105.0 parents in the program and 698.0 pupils, too.
# Hypothesis: 799.0 people were present in the program.
# Golden Label: contradiction

parents_premise = 105.0
pupils_premise = 698.0
total_people_hypothesis = 799.0

# the hypothesis refers to the total number of people, which can be computed from the premise
# compute the total number of people in the premise
total_people_premise = parents_premise + pupils_premise
if total_people_hypothesis == total_people_premise:
    # check if the total number of people in the hypothesis equals the total number of people from the premise
    label = "entailment"
else:
    # if the total number of people in the hypothesis does not equal the total number of people from the premise, we can infer a contradiction
    label = "contradiction"

print(label)

