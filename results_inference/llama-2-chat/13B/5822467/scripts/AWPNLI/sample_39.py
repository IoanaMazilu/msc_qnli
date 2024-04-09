drawer_crayons_premise = 7.0
mary_took_crayons_premise = 3.0
crayons_hypothesis = 0.0

# the hypothesis refers to the number of crayons, which are also mentioned in the premise
# compute the total number of crayons in the premise
total_crayons_premise = drawer_crayons_premise - mary_took_crayons_premise

if crayons_hypothesis <= total_crayons_premise:
    # check if the number of crayons in the hypothesis contradicts the number of crayons from the premise
    label = "contradiction"
elif crayons_hypothesis > total_crayons_premise:
    # check if the number of crayons in the hypothesis entails the number of crayons from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
