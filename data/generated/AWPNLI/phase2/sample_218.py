# Premise: White t-shirts can be purchased in packages of 6.0, and Mom buys 71.0 packages.
# Hypothesis: She will have 426.0 white t-shirts.
# Golden Label: entailment

packages_premise = 71.0
tshirts_per_package = 6.0
total_tshirts_hypothesis = 426.0

# the hypothesis refers to the total number of t-shirts, which can be computed from the premise
# compute the total number of t-shirts in the premise
total_tshirts_premise = packages_premise * tshirts_per_package
if total_tshirts_hypothesis != total_tshirts_premise:
    # check if the total number of t-shirts in the hypothesis contradicts the total number of t-shirts from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

