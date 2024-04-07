# Premise: Level-1 college graduates account for 10% of Listco's sales staff.
# Hypothesis: Level-less than 3 college graduates account for 10% of Listco's sales staff.
# Golden Label: entailment

sales_staff_premise = 10
sales_staff_hypothesis = 10

# The hypothesis talks about the percentage of level-less than 3 college graduates in sales staff, referenced also in the premise
if sales_staff_hypothesis != sales_staff_premise:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # If the hypothesis value does not contradict the premise value
    # we cannot infer entailment or contradiction because the levels of graduates are different
    label = "neutral"

print(label)

