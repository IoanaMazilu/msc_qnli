peanuts_premise = 1
peanuts_added_premise = 8
total_peanuts_premise = peanuts_premise + peanuts_added_premise

peanuts_hypothesis = 4
peanuts_added_hypothesis = 8
total_peanuts_hypothesis = peanuts_hypothesis + peanuts_added_hypothesis

# the hypothesis talks about the number of peanuts in a box, which is also referenced in the premise
if total_peanuts_hypothesis!= total_peanuts_premise:
    # check if the total number of peanuts in the hypothesis contradicts the total number of peanuts in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
