foods_premise = 1000
foods_hypothesis = 1000

# the hypothesis mentions the number of foods for which Google will showcase nutrition info, which is also mentioned in the premise
if foods_hypothesis!= foods_premise:
    # check if the number of foods in the hypothesis contradicts the number of foods reported in the premise
    label = "contradiction"
else:
    # if the number of foods in the hypothesis does not contradict the number of foods in the premise, we can infer entailment
    label = "entailment"

print(label)
