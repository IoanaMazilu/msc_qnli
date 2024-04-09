# the hypothesis and premise both talk about the product of X, Y and Z
# but the hypothesis changes the number 7 to 3

# define the variables
product_premise = 7
product_hypothesis = 3

# check if the product in the hypothesis contradicts the product in the premise
if product_premise!= product_hypothesis:
    label = "contradiction"
else:
    # if the product in the hypothesis does not contradict the product in the premise, we can infer entailment
    label = "entailment"

print(label)
