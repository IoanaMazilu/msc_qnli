# Premise: She turns around to head home after a short water break, how fast does Sasha need to ride, in miles per hour, to get home at 5 PM?
# Hypothesis: She turns around to head home after a short water break, how fast does Sasha need to ride, in miles per hour, to get home at more than 1 PM?
# Golden Label: entailment

home_time_premise = 5
home_time_hypothesis = 1

# the hypothesis refers to the time Sasha needs to get home, also mentioned in the premise
if home_time_hypothesis >= home_time_premise:
    # check if the hypothesis time contradicts the exact home time in the premise
    label = "contradiction"
elif home_time_hypothesis < home_time_premise:
    # if the hypothesis value is less than the premise value, it implies neutrality as any time before 5 PM cannot be explicitly inferred from the premise
    label = "neutral"

print(label)

