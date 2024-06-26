total_rent_premise = 160
total_rent_hypothesis = 760

# the hypothesis refers to the total amount paid for renting the tool, which is also mentioned in the premise
if total_rent_hypothesis!= total_rent_premise:
    # check if the total amount paid in the hypothesis contradicts the total amount paid in the premise
    label = "contradiction"
else:
    # if the total amount paid in the hypothesis does not contradict the total amount paid in the premise, we can infer entailment
    label = "entailment"

print(label)
