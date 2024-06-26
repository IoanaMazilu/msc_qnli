# Define variables for the premise and hypothesis
english_marks_premise = 55
history_marks_premise = 55
english_marks_hypothesis = 35
history_marks_hypothesis = 35

# Calculate the average of Suresh's marks in English and History
english_marks_average_premise = (english_marks_premise + history_marks_premise) / 2
history_marks_average_premise = (english_marks_premise + history_marks_premise) / 2

# Calculate the average of Suresh's marks in English and History
english_marks_average_hypothesis = (english_marks_hypothesis + history_marks_hypothesis) / 2
history_marks_average_hypothesis = (english_marks_hypothesis + history_marks_hypothesis) / 2

# Check if the hypothesis values contradict the premise
if english_marks_average_hypothesis!= english_marks_average_premise or history_marks_average_hypothesis!= history_marks_average_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
