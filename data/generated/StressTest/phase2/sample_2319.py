# Premise: If Kevin sells all his corn and cotton for a total of $640, then compute x.
# Hypothesis: If Kevin sells all his corn and cotton for a total of $more than 540, then compute x.
# Golden Label: entailment

total_sales_premise = 640
total_sales_hypothesis = 540

# the hypothesis refers to the total sales value mentioned in the premise
if total_sales_premise <= total_sales_hypothesis:
    # check if the estimate of 'total_sales_hypothesis' contradicts the total sales value in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

