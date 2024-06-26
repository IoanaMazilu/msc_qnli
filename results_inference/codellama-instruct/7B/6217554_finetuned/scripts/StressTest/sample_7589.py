# define variables for the scores in each subject
french_score = 86
geography_score = 75
art_score = 72
design_score = 63
history_score = 65

# define the total number of subjects
total_subjects = 5

# define the total number of marks
total_marks = 100

# define the average mark
average_mark = (french_score + geography_score + art_score + design_score + history_score) / total_subjects

# define the hypothesis average mark
hypothesis_average_mark = 86

# check if the hypothesis average mark contradicts the average mark
if hypothesis_average_mark >= average_mark:
    # check if the hypothesis average mark contradicts the average mark
    label = "contradiction"
else:
    # if the hypothesis average mark does not contradict the average mark, we can infer entailment
    label = "entailment"

print(label)
