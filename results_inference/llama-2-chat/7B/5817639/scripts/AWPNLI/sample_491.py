peanuts_premise = 5.0
peanuts_hypothesis = 1.0

# the hypothesis talks about the number of peanuts Carol has left, which is also mentioned in the premise
# compute the total number of peanuts Carol has
total_peanuts = peanuts_premise + peanuts_hypothesis

# check if the number of peanuts in the hypothesis contradicts the number of peanuts from the premise
if total_peanuts!= peanuts_hypothesis:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
