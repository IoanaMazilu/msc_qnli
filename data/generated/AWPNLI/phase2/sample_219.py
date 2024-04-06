# Premise: White t-shirts can be purchased in packages of 6.0, and Mom buys 71.0 packages.
# Hypothesis: She will have 422.0 white t-shirts.
# Golden Label: contradiction

packages_premise = 71.0
tshirts_per_package_premise = 6.0
total_tshirts_hypothesis = 422.0

# the hypothesis refers to the number of t-shirts, which is computed in the premise
# compute the total number of t-shirts in the premise
total_tshirts_premise = packages_premise * tshirts_per_package_premise
if total_tshirts_hypothesis != total_tshirts_premise:
    # check if the number of t-shirts in the hypothesis contradicts the number of t-shirts from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

