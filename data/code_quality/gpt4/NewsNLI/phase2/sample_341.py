speedboats_premise = 3 # Assuming the maximum number of speedboats
speedboats_hypothesis = 3 # Assuming the maximum number of speedboats

# the hypothesis mentions the number of speedboats chasing the Dutch ship, which is also referenced in the premise
# however, the hypothesis refers to the Dutch ship as a container ship and the source of information is different, which cannot be entailed from the premise
if speedboats_hypothesis != speedboats_premise:
    # check if the number of speedboats in the hypothesis contradicts the number of speedboats reported in the premise
    label = "contradiction"
else:
    # if the number of speedboats from the hypothesis does not contradict the number of speedboats in the premise, we can infer neutral
    label = "neutral"

print(label)
