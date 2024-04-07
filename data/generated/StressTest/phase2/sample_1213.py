# Premise: What is the minimum number of packages of Aero flight tees Bill must purchase to ensure that he has at least less than 30 golf tees for each member of his foursome, if he will buy no more than 3 packages of the generic golf tees?
# Hypothesis: What is the minimum number of packages of Aero flight tees Bill must purchase to ensure that he has at least 20 golf tees for each member of his foursome, if he will buy no more than 3 packages of the generic golf tees?
# Golden Label: neutral

tees_per_member_premise = 30
tees_per_member_hypothesis = 20
generic_tees_packages_premise = 3
generic_tees_packages_hypothesis = 3

# The hypothesis refers to the number of golf tees per member and the number of generic golf tee packages Bill must purchase, also mentioned in the premise
if tees_per_member_hypothesis >= tees_per_member_premise:
    # Check if the minimum number of golf tees per member in the hypothesis contradicts the estimate of less than 'tees_per_member_premise'
    label = "contradiction"
elif generic_tees_packages_hypothesis != generic_tees_packages_premise:
    # Check if the number of generic golf tee packages in the hypothesis contradicts the number of generic golf tee packages in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

