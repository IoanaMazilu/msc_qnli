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
