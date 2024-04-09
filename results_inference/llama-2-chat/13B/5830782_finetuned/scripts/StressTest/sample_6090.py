# The premise and hypothesis define the same condition for a "Sophie Germain" prime
# but the condition in the hypothesis is explicitly less than the one in the premise
condition_premise = 3 * 2 + 1
condition_hypothesis = 3 * 2 + 1

if condition_premise < condition_hypothesis:
    # check if the hypothesis condition contradicts the premise condition
    label = "contradiction"
else:
    # if the hypothesis condition does not contradict the premise condition, we can infer entailment
    label = "entailment"

print(label)
