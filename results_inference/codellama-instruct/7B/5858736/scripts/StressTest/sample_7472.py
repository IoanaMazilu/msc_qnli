# Define variables for the numerical entities in the premise and hypothesis
employees_level_1_premise = 72
employees_level_1_hypothesis = 62
college_graduates_premise = 30
college_graduates_hypothesis = 30

# Check if the hypothesis values contradict the premise values
if employees_level_1_hypothesis <= employees_level_1_premise:
    # The hypothesis value contradicts the premise value, so the hypothesis is a contradiction
    label = "contradiction"
elif college_graduates_hypothesis!= college_graduates_premise:
    # The number of college graduates in the hypothesis contradicts the number of college graduates in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
