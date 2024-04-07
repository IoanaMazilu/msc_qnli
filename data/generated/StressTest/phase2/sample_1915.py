# Premise: What is the minimum number of packages of Aero flight tees Bill must purchase to ensure that he has at least less than 40 golf tees for each member of his foursome, if he will buy no more than 2 packages of the generic golf tees?
# Hypothesis: What is the minimum number of packages of Aero flight tees Bill must purchase to ensure that he has at least 20 golf tees for each member of his foursome, if he will buy no more than 2 packages of the generic golf tees?
# Golden Label: neutral

golf_tees_premise = 40
golf_tees_hypothesis = 20
generic_packages_premise = 2
generic_packages_hypothesis = 2

# the hypothesis refers to the number of golf tees and generic packages mentioned in the premise
if golf_tees_premise < golf_tees_hypothesis:
    # check if the estimate of 'golf_tees_hypothesis' contradicts the number of golf tees in the premise
    label = "contradiction"
elif generic_packages_hypothesis != generic_packages_premise:
    # check if the number of generic packages in the hypothesis contradicts the number of generic packages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

