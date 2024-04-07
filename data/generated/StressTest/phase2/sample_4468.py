# Premise: Nagar the building were numbered from less than 5 to 100.
# Hypothesis: Nagar the building were numbered from 1 to 100.
# Golden Label: neutral

building_numbers_start_premise = 5
building_numbers_start_hypothesis = 1
building_numbers_end_premise = 100
building_numbers_end_hypothesis = 100

# the hypothesis refers to the numbering of the buildings mentioned in the premise
if building_numbers_start_hypothesis >= building_numbers_start_premise:
    # check if the start building number in the hypothesis contradicts the premise
    label = "contradiction"
elif building_numbers_end_hypothesis != building_numbers_end_premise:
    # check if the end building number in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

