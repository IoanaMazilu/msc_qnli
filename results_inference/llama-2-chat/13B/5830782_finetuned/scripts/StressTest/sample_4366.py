hours_premise = 60
hours_hypothesis = 40

# the hypothesis refers to the hours of work paid with x dollars, which is also mentioned in the premise
if hours_hypothesis > hours_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours in the premise
    label = "contradiction"
elif hours_hypothesis < hours_premise:
    # check if the number of hours in the hypothesis is less than the number of hours in the premise
    label = "entailment"
else:
    # if the number of hours in the hypothesis equals the number of hours in the premise,
    # it means the hypothesis is fully and explicitly entailed from the premise
    label = "entailment"

print(label)
