# marks obtained by the student in each subject according to the premise
geography_marks_premise = 56
history_marks_premise = 60
government_marks_premise = 72
art_marks_premise = 85
computer_science_marks_premise = 80
literature_marks_premise = 80

# marks obtained by the student in each subject according to the hypothesis
geography_marks_hypothesis = 26
history_marks_hypothesis = 60
government_marks_hypothesis = 72
art_marks_hypothesis = 85
computer_science_marks_hypothesis = 80
literature_marks_hypothesis = 80

# calculate the average marks according to the premise
average_marks_premise = (geography_marks_premise + history_marks_premise + government_marks_premise + art_marks_premise + computer_science_marks_premise + literature_marks_premise) / 6

# calculate the average marks according to the hypothesis
average_marks_hypothesis = (geography_marks_hypothesis + history_marks_hypothesis + government_marks_hypothesis + art_marks_hypothesis + computer_science_marks_hypothesis + literature_marks_hypothesis) / 6

# compare the average marks according to the premise and the hypothesis
if average_marks_premise!= average_marks_hypothesis:
    # if the average marks according to the premise and the hypothesis are different, it's a contradiction
    label = "contradiction"
else:
    # if the average marks according to the premise and the hypothesis are the same, it's an entailment
    label = "entailment"

print(label)
