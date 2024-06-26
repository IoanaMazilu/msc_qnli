english_mark_premise = 86
mathematics_mark_premise = 85
physics_mark_premise = 82
chemistry_mark_premise = 87
biology_mark_premise = 85

average_marks_premise = (english_mark_premise + mathematics_mark_premise + physics_mark_premise + chemistry_mark_premise + biology_mark_premise) / 5

average_marks_hypothesis = (less_than_86 + less_than_85 + less_than_82 + less_than_87 + less_than_85) / 5

# the hypothesis refers to the average marks of David mentioned in the premise
if average_marks_hypothesis >= average_marks_premise:
    # check if the estimate of 'average_marks_hypothesis' contradicts the average marks in the premise
    label = "contradiction"
elif average_marks_hypothesis < average_marks_premise:
    # check if the estimate of 'average_marks_hypothesis' is less than the average marks in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
