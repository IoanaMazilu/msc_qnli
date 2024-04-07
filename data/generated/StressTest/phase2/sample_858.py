# Premise: 4 buses runs between Chennai and Mysore.
# Hypothesis: less than 8 buses runs between Chennai and Mysore.
# Golden Label: entailment

buses_premise = 4
buses_hypothesis = 8

# the hypothesis refers to the number of buses running between Chennai and Mysore mentioned in the premise
if buses_premise >= buses_hypothesis:
    # check if the number of 'buses_premise' contradicts the estimate of less than 'buses_hypothesis'
    label = "contradiction"
elif buses_premise != buses_hypothesis - 1:
    # check if the number of buses in the premise is one less than 'buses_hypothesis'
    # if so, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)

