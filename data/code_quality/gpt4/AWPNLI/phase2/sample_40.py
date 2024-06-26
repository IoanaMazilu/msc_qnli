rulers_in_drawer_premise = 46.0
taken_rulers_premise = 25.0
rulers_in_drawer_hypothesis = 21.0

# the hypothesis refers to the number of rulers in the drawer after Tim took some, which is also mentioned in the premise
# compute the remaining number of rulers in the drawer in the premise
remaining_rulers_premise = rulers_in_drawer_premise - taken_rulers_premise
if rulers_in_drawer_hypothesis != remaining_rulers_premise:
    # check if the number of rulers in the drawer in the hypothesis contradicts the calculated number of rulers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
