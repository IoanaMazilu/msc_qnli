peanuts_in_box_premise = 4
peanuts_added = 12
total_peanuts_premise = peanuts_in_box_premise + peanuts_added

peanuts_in_box_hypothesis = 2
peanuts_added = 12
total_peanuts_hypothesis = peanuts_in_box_hypothesis + peanuts_added

# the hypothesis refers to the initial number of peanuts in a box and the number of peanuts added, which is also mentioned in the premise
if total_peanuts_premise!= total_peanuts_hypothesis:
    # check if the total number of peanuts in the hypothesis contradicts the total number of peanuts reported in the premise
    label = "contradiction"
elif peanuts_in_box_premise!= peanuts_in_box_hypothesis:
    # check if the initial number of peanuts in the hypothesis contradicts the initial number of peanuts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
