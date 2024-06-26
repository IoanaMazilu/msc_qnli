peanuts_premise = 4
peanuts_hypothesis = 7
added_peanuts_premise = 8
added_peanuts_hypothesis = 8

# the hypothesis refers to the number of peanuts in a box, which is also mentioned in the premise
# compute the total number of peanuts in the premise
total_peanuts_premise = peanuts_premise + added_peanuts_premise

if peanuts_hypothesis!= total_peanuts_premise:
    # check if the number of peanuts in the hypothesis contradicts the total number of peanuts from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
