# Premise: If Anne’s speed were doubled, they could clean their house in 3 hours working at their respective rates.
# Hypothesis: If Anne’s speed were doubled, they could clean their house in less than 5 hours working at their respective rates.
# Golden Label: entailment

clean_time_premise = 3
clean_time_hypothesis = 5

# the hypothesis refers to the cleaning time mentioned in the premise
if clean_time_premise >= clean_time_hypothesis:
    # check if the estimated 'clean_time_hypothesis' contradicts the cleaning time in the premise
    label = "contradiction"
elif clean_time_hypothesis > clean_time_premise:
    # check if the cleaning time in the hypothesis is greater than the cleaning time reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "contradiction"

print(label)

