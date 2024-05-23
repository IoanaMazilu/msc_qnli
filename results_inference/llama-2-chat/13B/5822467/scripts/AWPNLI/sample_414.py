drawer_crayons_premise = 7.0
mary_added_crayons_premise = 3.0
total_crayons_hypothesis = 10.0

# compute the total number of crayons in the premise
total_crayons_premise = drawer_crayons_premise + mary_added_crayons_premise

if total_crayons_hypothesis > total_crayons_premise:
    # check if the number of crayons in the hypothesis contradicts the number of crayons from the premise
    label = "contradiction"
elif total_crayons_hypothesis < total_crayons_premise:
    # check if the number of crayons in the hypothesis is less than the estimate in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)