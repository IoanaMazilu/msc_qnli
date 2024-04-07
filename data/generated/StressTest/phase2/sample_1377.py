# Premise: If Bob runs at a constant rate of 8 minutes per mile, how many miles farther south can he run and still be able to return to the parking lot in 50 minutes?
# Hypothesis: If Bob runs at a constant rate of more than 6 minutes per mile, how many miles farther south can he run and still be able to return to the parking lot in 50 minutes?
# Golden Label: entailment

run_rate_premise = 8
run_rate_hypothesis = 6
time_limit = 50

# the hypothesis refers to the running rate and time limit mentioned in the premise
if run_rate_premise < run_rate_hypothesis:
    # check if the 'run_rate_premise' contradicts the run rate in the hypothesis
    label = "contradiction"
elif run_rate_premise == run_rate_hypothesis:
    # check if the 'run_rate_premise' equals the run rate in the hypothesis
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, 
    # but also cannot be fully entailed from the premise, we infer neutrality
    label = "neutral"

print(label)

