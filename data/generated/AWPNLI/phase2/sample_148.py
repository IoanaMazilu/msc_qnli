# Premise: There were 105.0 parents in the program and 698.0 pupils, too.
# Hypothesis: 803.0 people were present in the program.
# Golden Label: entailment

parents_premise = 105.0
pupils_premise = 698.0
total_people_hypothesis = 803.0

# the hypothesis refers to the total number of people, which is the sum of parents and pupils in the premise
# compute the total number of people in the premise
total_people_premise = parents_premise + pupils_premise
if total_people_hypothesis != total_people_premise:
    # check if the total number of people in the hypothesis contradicts the total number of people from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

