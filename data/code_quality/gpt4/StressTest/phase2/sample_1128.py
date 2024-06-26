year_premise = 2003
year_hypothesis = 7003

# the hypothesis refers to a year before the one mentioned in the premise
if year_hypothesis <= year_premise:
    # the premise gives us information only for the year 2003, so we can't infer anything about other years
    label = "neutral"
else:
    # if the year in the hypothesis is after the year in the premise, it contradicts the premise
    label = "contradiction"

print(label)
