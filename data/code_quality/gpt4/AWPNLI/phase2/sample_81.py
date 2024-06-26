mike_apples_premise = 7.0
nancy_apples_premise = 3.0
keith_apples_premise = 6.0
total_apples_hypothesis = 20.0

# the hypothesis refers to the total number of apples picked, which are also mentioned in the premise
# compute the total number of apples in the premise
total_apples_premise = mike_apples_premise + nancy_apples_premise + keith_apples_premise
if total_apples_hypothesis != total_apples_premise:
    # check if the total number of apples in the hypothesis contradicts the total number of apples from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
