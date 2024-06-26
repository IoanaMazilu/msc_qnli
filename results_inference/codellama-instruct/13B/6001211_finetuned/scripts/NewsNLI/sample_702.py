positive_view_premise = 69
positive_view_hypothesis = 12

# the hypothesis mentions the percentage of people who have a positive view of the United States, which is also referenced in the premise
# however, the percentage in the hypothesis is different from the percentage in the premise
if positive_view_hypothesis > positive_view_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer neutrality
    label = "neutral"

print(label)
