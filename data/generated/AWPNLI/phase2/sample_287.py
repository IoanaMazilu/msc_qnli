# Premise: The school cafeteria had 38.0 apples, and they used 20.0 to make lunch for the students and then bought 28.0 more.
# Hypothesis: They would have 43.0 apples.
# Golden Label: contradiction

initial_apples_premise = 38.0
used_apples_premise = 20.0
bought_apples_premise = 28.0
total_apples_hypothesis = 43.0

# the hypothesis refers to the total number of apples, which is also mentioned in the premise
# compute the total number of apples in the premise
total_apples_premise = initial_apples_premise - used_apples_premise + bought_apples_premise
if total_apples_hypothesis != total_apples_premise:
    # check if the total number of apples in the hypothesis contradicts the total number of apples from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

