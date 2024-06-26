 herbank_quarter_premise = 21.0
given_quarter_premise = 49.0
total_quarter_hypothesis = 70.0

# the hypothesis refers to the total number of quarters, which are also mentioned in the premise
# compute the total number of quarters in the premise
total_quarter_premise = herbank_quarter_premise + given_quarter_premise
if total_quarter_hypothesis!= total_quarter_premise:
    # check if the total number of quarters in the hypothesis contradicts the total number of quarters from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"    

print(label)
