geography_marks_premise = 56
history_marks_premise = 60
government_marks_premise = 72
art_marks_premise = 80
computer_science_marks_premise = 85
modern_literature_marks_premise = 80

hypothesis_marks = [26, 60, 72, 85, 80]

# define variables with representative names for the numerical entities in both inputs
geography_marks_hypothesis = hypothesis_marks[0]
history_marks_hypothesis = hypothesis_marks[1]
government_marks_hypothesis = hypothesis_marks[2]
art_marks_hypothesis = hypothesis_marks[3]
computer_science_marks_hypothesis = hypothesis_marks[4]
modern_literature_marks_hypothesis = hypothesis_marks[5]

# extract all quantities as valid numbers (integers or floats)
geography_marks_premise = int(geography_marks_premise)
history_marks_premise = int(history_marks_premise)
government_marks_premise = int(government_marks_premise)
art_marks_premise = int(art_marks_premise)
computer_science_marks_premise = int(computer_science_marks_premise)
modern_literature_marks_premise = int(modern_literature_marks_premise)

for i, mark in enumerate(hypothesis_marks):
    if mark > geography_marks_premise:
        # check if the estimate of 'geography_marks_hypothesis' contradicts the number of marks reported in the premise
        label = "contradiction"
        break
    elif mark!= history_marks_premise:
        # check if the number of marks in the hypothesis contradicts the number of marks reported in the premise
        label = "contradiction"
        break
    elif mark > government_marks_premise:
        # check if the estimate of 'government_marks_hypothesis' contradicts the number of marks reported in the premise
        label = "contradiction"
        break
    elif mark!= art_marks_premise:
        # check if the number of marks in the hypothesis contradicts the number of marks reported in the premise
        label = "contradiction"
        break
    elif mark > computer_science_marks_premise:
        # check if the estimate of 'computer_science_marks_hypothesis' contradicts the number of marks reported in the premise
        label = "contradiction"
        break
    elif mark!= modern_literature_marks_premise:
        # check if the number of marks in the hypothesis contradicts the number of marks reported in the premise
        label = "contradiction"
        break
    else:
        # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
        label = "entailment"

print(label)
