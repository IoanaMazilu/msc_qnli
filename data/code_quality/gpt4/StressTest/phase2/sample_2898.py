peanuts_premise = 4
peanuts_added = 4
total_peanuts_premise = peanuts_premise + peanuts_added

peanuts_hypothesis = 8
total_peanuts_hypothesis = peanuts_hypothesis + peanuts_added

# the hypothesis refers to the number of peanuts in the box and the number of added peanuts mentioned in the premise
if total_peanuts_premise != total_peanuts_hypothesis:
    # check if the total number of peanuts in the hypothesis contradicts with the total number of peanuts in the premise
    label = "contradiction"
elif peanuts_hypothesis >= peanuts_premise:
    # check if the number of peanuts in the hypothesis contradicts the number of peanuts in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
