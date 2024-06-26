percentage_premise = 15
percentage_hypothesis = 10

# the hypothesis mentions the percentage of Saudis with a favorable view of al Qaeda, which is also referenced in the premise
if percentage_hypothesis > percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer neutrality
    label = "neutral"

print(label)
