english_marks_premise = 15
history_marks_premise = 15
average_premise = (english_marks_premise + history_marks_premise) / 2

english_marks_hypothesis = 55
history_marks_hypothesis = 55
average_hypothesis = (english_marks_hypothesis + history_marks_hypothesis) / 2

# the hypothesis refers to the average of Suresh's marks in English and History
if average_hypothesis > average_premise:
    # the hypothesis explicitly entails the premise
    label = "entailment"
elif average_hypothesis <= average_premise:
    # the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"
else:
    # at least one aspect in the hypothesis contradicts the premise
    label = "contradiction"

print(label)
