recall_cartons_premise = 2498
deaths_premise = 13
deaths_hypothesis = 13

# the hypothesis mentions the number of deaths caused by the same bacteria, which is also mentioned in the premise
# however, the hypothesis does not mention the number of recalled cartons, which is specified in the premise
if deaths_hypothesis!= deaths_premise:
    # check if the number of deaths in the hypothesis contradicts the number of deaths reported in the premise
    label = "contradiction"
else:
    # if the number of deaths in the hypothesis does not contradict the number of deaths in the premise, we can infer neutrality
    label = "neutral"

print(label)
