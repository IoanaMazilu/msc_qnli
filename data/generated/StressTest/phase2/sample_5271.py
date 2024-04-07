# Premise: In one day, Juan sends Keith three times as many messages as he sends Laurence, and Laurence sends Missy 2 times as many messages as he receives from Juan.
# Hypothesis: In one day, Juan sends Keith three times as many messages as he sends Laurence, and Laurence sends Missy more than 1 times as many messages as he receives from Juan.
# Golden Label: entailment

# defining ratio of messages sent
juan_keith_to_laurence_premise = 3
laurence_missy_to_juan_premise = 2

juan_keith_to_laurence_hypothesis = 3
laurence_missy_to_juan_hypothesis = 1

# comparing ratios of messages sent as mentioned in premise and hypothesis
if juan_keith_to_laurence_premise != juan_keith_to_laurence_hypothesis:
    # check if the ratio of messages Juan sends to Keith and Laurence contradicts the premise
    label = "contradiction"
elif laurence_missy_to_juan_hypothesis >= laurence_missy_to_juan_premise:
    # check if the ratio of messages Laurence sends to Missy and receives from Juan contradicts the premise
    label = "contradiction"
else:
    # if the ratios mentioned in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

