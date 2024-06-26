people_bondage_premise = 12300000
people_bondage_hypothesis = 12300000

# The hypothesis mentions the number of people laboring in bondage according to the International Labour Organization, which is also indicated in the premise
if people_bondage_hypothesis != people_bondage_premise:
    # Check if the number of people laboring in bondage in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
