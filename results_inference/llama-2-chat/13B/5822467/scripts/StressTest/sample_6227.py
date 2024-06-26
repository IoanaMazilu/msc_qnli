boys_premise = 300
girls_premise = 240

# Define variables for the hypotheses
boys_hypothesis = None
girls_hypothesis = None

# Parse the hypotheses
if "more than" in hypothesis:
    hypothesis_parts = hypothesis.split(" more than ")
    boys_hypothesis = int(hypothesis_parts[0])
    girls_hypothesis = int(hypothesis_parts[1])
else:
    # If the hypothesis does not contain "more than", assume it is a single number
    boys_hypothesis = int(hypothesis)
    girls_hypothesis = int(hypothesis)

# Check if the number of boys in the hypothesis contradicts the premise
if boys_hypothesis > boys_premise:
    label = "contradiction"
elif boys_hypothesis < boys_premise:
    label = "entailment"
else:
    # The number of boys in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

# Check if the number of girls in the hypothesis contradicts the premise
if girls_hypothesis > girls_premise:
    label = "contradiction"
elif girls_hypothesis < girls_premise:
    label = "entailment"
else:
    # The number of girls in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
