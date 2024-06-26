doctors_premise = 5
doctors_hypothesis = 5
pharmacists_premise = 2
pharmacists_hypothesis = 2

# the hypothesis mentions the number of arrested doctors and pharmacists, which are also mentioned in the premise
if doctors_hypothesis != doctors_premise:
    # check if the number of doctors in the hypothesis contradicts the number of doctors in the premise
    label = "contradiction"
elif pharmacists_hypothesis != pharmacists_premise:
    # check if the number of pharmacists from the hypothesis contradicts the number of pharmacists in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
