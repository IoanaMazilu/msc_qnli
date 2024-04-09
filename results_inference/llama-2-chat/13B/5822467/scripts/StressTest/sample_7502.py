pat_speed_premise = 9
pat_speed_hypothesis = float(input("Enter Pat's speed: "))
cara_speed_premise = 5
cara_speed_hypothesis = float(input("Enter Cara's speed: "))

# check if Pat's speed in the hypothesis contradicts the premise
if pat_speed_hypothesis > pat_speed_premise:
    label = "contradiction"
elif cara_speed_hypothesis == cara_speed_premise:
    # check if the estimate of Cara's speed in the premise is consistent with the hypothesis
    label = "neutral"
else:
    # the hypothesis refers to the speed of both runners, which are mentioned in the premise
    label = "entailment"

print(label)
