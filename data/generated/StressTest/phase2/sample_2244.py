# Premise: Level-1 college graduates account for 15% of Listco's sales staff.
# Hypothesis: Level-less than 2 college graduates account for 15% of Listco's sales staff.
# Golden Label: entailment

graduates_percentage_premise = 15
graduates_percentage_hypothesis = 15

# the hypothesis refers to the percentage of college graduates in Listco's sales staff mentioned in the premise
if graduates_percentage_premise != graduates_percentage_hypothesis:
    # check if the percentage of college graduates in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # Level-1 college graduates are a subset of Level-2 or less college graduates
    # so the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

