# Premise: In less than 7003, the number of girls attending Jefferson High School was equal to the number of boys.
# Hypothesis: In 2003, the number of girls attending Jefferson High School was equal to the number of boys.
# Golden Label: neutral

year_premise = 7003
year_hypothesis = 2003

# the hypothesis refers to a year within the time frame mentioned in the premise
if year_hypothesis >= year_premise:
    # check if the year in the hypothesis contradicts the 'less than year_premise' from the premise
    label = "contradiction"
else:
    # the premise gives a period until 'year_premise'
    # any year less than 'year_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

