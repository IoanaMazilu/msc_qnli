marks_premise = [66, 75, 52, 68, 89]
marks_hypothesis = [86, 75, 52, 68, 89]

# define variables for each subject's marks in the premise and hypothesis
lit_premise = marks_premise[0]
lit_hypothesis = marks_hypothesis[0]
his_premise = marks_premise[1]
his_hypothesis = marks_hypothesis[1]
econ_premise = marks_premise[2]
econ_hypothesis = marks_hypothesis[2]
pe_premise = marks_premise[3]
pe_hypothesis = marks_hypothesis[3]
art_premise = marks_premise[4]
art_hypothesis = marks_hypothesis[4]

# compare the marks in each subject
lit_comp = lit_hypothesis >= lit_premise
his_comp = his_hypothesis >= his_premise
econ_comp = econ_hypothesis >= econ_premise
pe_comp = pe_hypothesis >= pe_premise
art_comp = art_hypothesis >= art_premise

# check if any of the comparisons contradict each other
if not (lit_comp and his_comp and econ_comp and pe_comp and art_comp):
    # at least one aspect in the hypothesis contradicts the premise
    label = "contradiction"
elif lit_comp and his_comp and econ_comp and pe_comp and art_comp:
    # the hypothesis can be fully and explicitly entailed from the premise
    label = "entailment"
else:
    # the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
