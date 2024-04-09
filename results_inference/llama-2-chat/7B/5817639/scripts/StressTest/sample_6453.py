# Premise: Calculate the average mark scored by Andrea if he had the following scores in an examination: 66, 60, 72, 77, 55 and 85 marks (out of 100) in English, Mathematics, Chemistry, Biology, French Language and Physics respectively?
premise_marks = [66, 60, 72, 77, 55, 85]

# Hypothesis: Calculate the average mark scored by Andrea if he had the following scores in an examination: less than 76, 60, 72, 77, 55 and 85 marks (out of 100) in English, Mathematics, Chemistry, Biology, French Language and Physics respectively?
hypothesis_marks = [76, 60, 72, 77, 55, 85]

# calculate the average mark for the premise
average_premise_mark = sum(premise_marks) / len(premise_marks)

# calculate the average mark for the hypothesis
average_hypothesis_mark = sum(hypothesis_marks) / len(hypothesis_marks)

# check if the hypothesis value contradicts the estimate of the average mark in the premise
if hypothesis_marks[0] < average_premise_mark:
    label = "contradiction"
else:
    # the premise gives only an estimate for the average mark
    # any average mark greater than 'average_premise_mark' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
