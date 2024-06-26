building_numbers_start_premise = 1
building_numbers_end_premise = 100
building_numbers_start_hypothesis = 1
building_numbers_end_hypothesis = 100

# the hypothesis mentions the range of building numbers in Nagar, which is also mentioned in the premise
if building_numbers_start_hypothesis < building_numbers_start_premise:
    # check if the start of the building numbers in the hypothesis contradicts the start of the building numbers in the premise
    label = "contradiction"
elif building_numbers_end_hypothesis != building_numbers_end_premise:
    # check if the end of the building numbers in the hypothesis contradicts the end of the building numbers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
