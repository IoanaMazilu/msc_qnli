# Premise: Which of the following could be the total student population at Jefferson High School in 2004?
# Hypothesis: Which of the following could be the total student population at Jefferson High School in 3004?
# Golden Label: contradiction

year_premise = 2004
year_hypothesis = 3004

# the hypothesis refers to the year which is also mentioned in the premise
if year_hypothesis != year_premise:
    # check if the year in the hypothesis contradicts the year mentioned in the premise
    label = "contradiction"
else:
    # the premise does not provide any numerical information to compare with
    label = "neutral"

print(label)

