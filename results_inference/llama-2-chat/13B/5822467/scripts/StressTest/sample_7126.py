jogging_premise = float(input("Enter the distance from home Aaron can jog in premise: "))
jogging_hypothesis = float(input("Enter the distance from home Aaron can jog in hypothesis: "))
walking_premise = float(input("Enter the time Aaron spends walking in premise: "))
walking_hypothesis = float(input("Enter the time Aaron spends walking in hypothesis: "))

# Convert the input values to integers for comparison
jogging_premise = int(jogging_premise)
jogging_hypothesis = int(jogging_hypothesis)
walking_premise = int(walking_premise)
walking_hypothesis = int(walking_hypothesis)

# Check if the hypothesis contradicts the premise
if jogging_hypothesis > jogging_premise:
    label = "contradiction"
elif walking_hypothesis > walking_premise:
    label = "contradiction"
else:
    # Check if the hypothesis values are consistent with the premise
    if jogging_hypothesis >= jogging_premise and walking_hypothesis >= walking_premise:
        label = "entailment"
    else:
        label = "neutral"

print(label)
