# Premise: Nagar the building were numbered from 1 to 100.
# Hypothesis: Nagar the building were numbered from less than 5 to 100.
# Golden Label: entailment

building_number_start_premise = 1
building_number_start_hypothesis = 5
building_number_end_premise = 100
building_number_end_hypothesis = 100

# the hypothesis talks about the range of building numbers in Nagar, which is also referenced in the premise
if building_number_start_hypothesis > building_number_start_premise:
    # check if the starting building number in the hypothesis contradicts the starting building number in the premise
    label = "contradiction"
elif building_number_end_hypothesis != building_number_end_premise:
    # check if the ending building number in the hypothesis contradicts the ending building number in the premise
    label = "contradiction"
else:
    # if the range of building numbers in the hypothesis does not contradict the range in the premise, we can infer entailment
    label = "entailment"

print(label)

