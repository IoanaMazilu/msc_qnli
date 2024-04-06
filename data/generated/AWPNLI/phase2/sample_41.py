# Premise: There are 46.0 rulers in the drawer and Tim took 25.0 rulers from the drawer.
# Hypothesis: 22.0 rulers are now in the drawer.
# Golden Label: contradiction

rulers_in_drawer_premise = 46.0
rulers_taken_premise = 25.0
rulers_in_drawer_hypothesis = 22.0

# the hypothesis refers to the number of rulers, which are also mentioned in the premise
# compute the remaining number of rulers in the premise
remaining_rulers_premise = rulers_in_drawer_premise - rulers_taken_premise
if rulers_in_drawer_hypothesis != remaining_rulers_premise:
    # check if the number of rulers in the hypothesis contradicts the number of rulers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

