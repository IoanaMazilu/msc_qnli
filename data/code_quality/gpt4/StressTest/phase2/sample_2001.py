years_future_premise = 5
years_future_hypothesis = 2

# the hypothesis is about the same future scenario mentioned in the premise
# but, the timing differs
if years_future_hypothesis >= years_future_premise:
    # check if the hypothesis contradicts the specific time in the future stated in the premise
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise, but it does not explicitly follow from the premise either
    label = "neutral"

print(label)
