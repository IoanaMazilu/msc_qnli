# Premise: What is the minimum number of packages of Aero flight tees Bill must purchase to ensure that he has at least 10 golf tees for each member of his foursome, if he will buy no more than 2 packages of the generic golf tees?
# Hypothesis: What is the minimum number of packages of Aero flight tees Bill must purchase to ensure that he has at least less than 40 golf tees for each member of his foursome, if he will buy no more than 2 packages of the generic golf tees?
# Golden Label: entailment

golf_tees_needed_premise = 10
members_foursome = 4
golf_tees_needed_hypothesis = 40

# The hypothesis states the minimum number of golf tees Bill must purchase for each member of his foursome
if golf_tees_needed_hypothesis != golf_tees_needed_premise * members_foursome:
    # checking if the number of golf tees in the hypothesis contradicts the number of golf tees mentioned in the premise
    label = "contradiction"
else:
    # if the number of golf tees in the hypothesis does not contradict the number mentioned in the premise
    label = "entailment"

print(label)

