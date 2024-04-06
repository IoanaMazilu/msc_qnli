# Premise: The town of Milburg has 5256.0 grown-ups and children and 2987.0 are children.
# Hypothesis: 2269.0 adults live in Milburg.
# Golden Label: entailment

total_people_premise = 5256.0
children_premise = 2987.0
adults_hypothesis = 2269.0

# the hypothesis refers to the number of adults, which can be inferred from the premise by subtracting the number of children from the total number of people
# calculate the number of adults in the premise
adults_premise = total_people_premise - children_premise
if adults_hypothesis != adults_premise:
    # check if the number of adults in the hypothesis contradicts the number of adults inferred from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

