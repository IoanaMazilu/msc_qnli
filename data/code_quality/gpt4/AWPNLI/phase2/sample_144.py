girls_premise = 542.0
boys_premise = 387.0
pupils_hypothesis = 929.0

# the hypothesis refers to the total number of pupils, which are also mentioned in the premise
# compute the total number of pupils in the premise
total_pupils_premise = girls_premise + boys_premise
if pupils_hypothesis != total_pupils_premise:
    # check if the total number of pupils in the hypothesis contradicts the total number of pupils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
