# Premise: There are 11.0 rulers and 34.0 crayons in the drawer and Tim placed 14.0 rulers in the drawer.
# Hypothesis: 25.0 rulers are now there in all.
# Golden Label: entailment

rulers_premise = 11.0
crayons_premise = 34.0
added_rulers_premise = 14.0
total_rulers_hypothesis = 25.0

# the hypothesis refers to the total number of rulers, which are also mentioned in the premise
# compute the total number of rulers in the premise
total_rulers_premise = rulers_premise + added_rulers_premise
if total_rulers_hypothesis != total_rulers_premise:
    # check if the total number of rulers in the hypothesis contradicts the total number of rulers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

