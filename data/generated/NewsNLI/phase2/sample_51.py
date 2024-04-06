# Premise: Emmanuel Miller, 16, and Zachary Watson, 17 are charged as adults, police said.
# Hypothesis: Two teen suspects charged as adults.
# Golden Label: entailment

emmanuel_age_premise = 16
zachary_age_premise = 17
total_teens_premise = 2
total_teens_hypothesis = 2

# the hypothesis mentions two teens being charged as adults, which matches with the premise
if total_teens_hypothesis != total_teens_premise:
    # check if the number of teens charged as adults in the hypothesis contradicts the number of teens charged as adults in the premise
    label = "contradiction"
else:
    # if the hypothesis number of teens do not contradict the premise number of teens, we can infer entailment
    label = "entailment"

print(label)

