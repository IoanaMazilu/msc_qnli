# Premise: Raman mixed 27 kg of butter at Rs.
# Hypothesis: Raman mixed 77 kg of butter at Rs.
# Golden Label: contradiction

butter_weight_premise = 27
butter_weight_hypothesis = 77

# the hypothesis talks about the weight of butter mixed by Raman, referenced also in the premise
if butter_weight_hypothesis != butter_weight_premise:
    # check if the weight of butter in the hypothesis contradicts the weight of butter reported in the premise
    label = "contradiction"
else:
    # if the weight of butter in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

