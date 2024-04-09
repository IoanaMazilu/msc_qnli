# define variables with representative names for the numerical entities in both inputs
geography_marks_premise = 56
geography_marks_hypothesis = 0
history_marks_premise = 60
history_marks_hypothesis = 0
government_marks_premise = 72
government_marks_hypothesis = 0
art_marks_premise = 80
art_marks_hypothesis = 0
computer_sci_marks_premise = 85
computer_sci_marks_hypothesis = 0
modern_lit_marks_premise = 80
modern_lit_marks_hypothesis = 0

# extract all quantities as valid numbers (integers or floats)
geography_marks_premise = int(geography_marks_premise)
history_marks_premise = int(history_marks_premise)
government_marks_premise = int(government_marks_premise)
art_marks_premise = int(art_marks_premise)
computer_sci_marks_premise = int(computer_sci_marks_premise)
modern_lit_marks_premise = int(modern_lit_marks_premise)

geography_marks_hypothesis = int(geography_marks_hypothesis)
history_marks_hypothesis = int(history_marks_hypothesis)
government_marks_hypothesis = int(government_marks_hypothesis)
art_marks_hypothesis = int(art_marks_hypothesis)
computer_sci_marks_hypothesis = int(computer_sci_marks_hypothesis)
modern_lit_marks_hypothesis = int(modern_lit_marks_hypothesis)

# compare the variables
if geography_marks_hypothesis < geography_marks_premise:
    # the hypothesis refers to a lower value of marks in Geography
    label = "entailment"
elif history_marks_hypothesis < history_marks_premise:
    # the hypothesis refers to a lower value of marks in History
    label = "entailment"
elif government_marks_hypothesis < government_marks_premise:
    # the hypothesis refers to a lower value of marks in Government
    label = "entailment"
elif art_marks_hypothesis < art_marks_premise:
    # the hypothesis refers to a lower value of marks in Art
    label = "entailment"
elif computer_sci_marks_hypothesis < computer_sci_marks_premise:
    # the hypothesis refers to a lower value of marks in Computer Science
    label = "entailment"
elif modern_lit_marks_hypothesis < modern_lit_marks_premise:
    # the hypothesis refers to a lower value of marks in Modern Literature
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
