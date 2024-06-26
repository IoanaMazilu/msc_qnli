jazmin_dolls_premise = 1209.0
geraldine_dolls_premise = 2186.0
total_dolls_hypothesis = 3397.0

# the hypothesis refers to the total number of dolls, which is the sum of the dolls from the premise
# compute the total number of dolls in the premise
total_dolls_premise = jazmin_dolls_premise + geraldine_dolls_premise
if total_dolls_hypothesis != total_dolls_premise:
    # check if the number of dolls in the hypothesis contradicts the number of dolls from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
