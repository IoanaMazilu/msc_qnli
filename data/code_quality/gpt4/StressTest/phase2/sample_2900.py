initial_peanuts_premise = 4
additional_peanuts_premise = 4
initial_peanuts_hypothesis = 5
additional_peanuts_hypothesis = 4

# the hypothesis talks about the number of peanuts in a box which Mary increases, also referenced in the premise

if initial_peanuts_premise != initial_peanuts_hypothesis or additional_peanuts_premise != additional_peanuts_hypothesis:
    # check if the number of initial peanuts or the number of additional peanuts in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
