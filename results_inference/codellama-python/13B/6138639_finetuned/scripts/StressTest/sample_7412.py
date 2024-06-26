butter_kg_premise = 27
butter_kg_hypothesis = 77

# the hypothesis talks about the quantity of butter mixed by Raman, referenced also in the premise
if butter_kg_hypothesis!= butter_kg_premise:
    # check if the quantity of butter in the hypothesis contradicts the quantity of butter reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
