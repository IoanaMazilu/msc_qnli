peanuts_premise = 1
peanuts_hypothesis = 4

# the hypothesis talks about the number of peanuts in a box, which is also mentioned in the premise
if peanuts_hypothesis <= peanuts_premise:
    # check if the number of peanuts in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the number of peanuts in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
