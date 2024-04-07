# Premise: What is the minimum number of packages of Aero flight tees Bill must purchase to ensure that he has at least 20 golf tees for each member of his foursome, if he will buy no more than 3 packages of the generic golf tees?
# Hypothesis: What is the minimum number of packages of Aero flight tees Bill must purchase to ensure that he has at least more than 20 golf tees for each member of his foursome, if he will buy no more than 3 packages of the generic golf tees?
# Golden Label: contradiction

golf_tees_premise = 20
golf_tees_hypothesis = 20
packages_generic_tees_premise = 3
packages_generic_tees_hypothesis = 3

# the hypothesis refers to the number of golf tees and packages of generic golf tees mentioned in the premise
if golf_tees_hypothesis <= golf_tees_premise:
    # check if the estimate of 'golf_tees_hypothesis' contradicts the number of golf tees in the premise
    label = "contradiction"
elif packages_generic_tees_hypothesis != packages_generic_tees_premise:
    # check if the number of packages of generic golf tees in the hypothesis contradicts the number of packages of generic golf tees reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

