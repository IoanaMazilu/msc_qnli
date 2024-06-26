seating_people_premise = 8
seating_people_hypothesis = 6

# the hypothesis refers to the number of people that can be seated on a bench, also referenced in the premise
if seating_people_hypothesis == seating_people_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif seating_people_hypothesis > seating_people_premise:
    # check if the number of people in the hypothesis is greater than the number of people in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
