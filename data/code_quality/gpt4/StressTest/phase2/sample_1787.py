average_marks_premise = 18
average_marks_hypothesis = 48

# the hypothesis refers to the difference in average marks between different subjects mentioned in the premise
if average_marks_hypothesis < average_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_marks_premise'
    label = "contradiction"
elif average_marks_hypothesis > average_marks_premise:
    # if the difference in average marks in the hypothesis is greater than in the premise
    # it does not contradict the premise, but it cannot be explicitly entailed from it, thus it's neutral
    label = "neutral"
else:
    # if the difference in average marks in the hypothesis equals the one in the premise
    # it can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)
