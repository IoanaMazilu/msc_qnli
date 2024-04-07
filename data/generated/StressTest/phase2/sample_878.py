# Premise: Winson will arrange 6 people of 6 different heights for photograph by placing them in two rows of three so that each person in the first row is standing is standing in front of someone in the second row.
# Hypothesis: Winson will arrange less than 6 people of 6 different heights for photograph by placing them in two rows of three so that each person in the first row is standing is standing in front of someone in the second row.
# Golden Label: contradiction

people_arranged_premise = 6
people_arranged_hypothesis = 6

# the hypothesis talks about the number of people arranged by Winson, referenced also in the premise
if people_arranged_hypothesis < people_arranged_premise:
    # check if the hypothesis value contradicts the number of people arranged in the premise
    label = "contradiction"
elif people_arranged_hypothesis > people_arranged_premise:
    # check if the hypothesis value contradicts the number of people arranged in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

