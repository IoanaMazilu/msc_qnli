us_manufacturing_percentage_premise = 0.80
us_manufacturing_percentage_hypothesis = 0.80

# the hypothesis mentions the percentage of parts made in the U.S., which is also referenced in the premise
if us_manufacturing_percentage_hypothesis <= us_manufacturing_percentage_premise:
    # check if the percentage of parts made in the U.S. in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the percentage of parts made in the U.S. in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
