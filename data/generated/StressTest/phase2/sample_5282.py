# Premise: What is the minimum number of packages of Aero flight tees Bill must purchase to ensure that he has at least 10 golf tees for each member of his foursome, if he will buy no more than 3 packages of the generic golf tees?
# Hypothesis: What is the minimum number of packages of Aero flight tees Bill must purchase to ensure that he has at least 30 golf tees for each member of his foursome, if he will buy no more than 3 packages of the generic golf tees?
# Golden Label: contradiction

tees_per_member_premise = 10
tees_per_member_hypothesis = 30
packages_generic_tees = 3

# the hypothesis refers to the number of golf tees per member, also mentioned in the premise
if tees_per_member_hypothesis < tees_per_member_premise:
    # check if the hypothesis value contradicts the premise estimate of 'tees_per_member_premise'
    label = "contradiction"
elif tees_per_member_hypothesis > tees_per_member_premise:
    # check if the hypothesis value contradicts the premise estimate of 'tees_per_member_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of golf tees per member
    # the same number of tees per member in the hypothesis can be explicitly entailed from the premise
    # but the premise and the hypothesis are asking questions, so we cannot definitively infer entailment
    label = "neutral"

print(label)

