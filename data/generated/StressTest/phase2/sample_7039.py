# Premise: Calculate the average marks of a student who obtained more than 26, 60, 72, 85 and 80 marks (out of 100) in Geography, History and Government, Art, Computer Science and Modern Literature?
# Hypothesis: Calculate the average marks of a student who obtained 56, 60, 72, 85 and 80 marks (out of 100) in Geography, History and Government, Art, Computer Science and Modern Literature?
# Golden Label: neutral

geo_hist_gov_premise = 26
geo_hist_gov_hypothesis = 56
art_premise = art_hypothesis = 60
comp_sci_premise = comp_sci_hypothesis = 72
lit_premise = lit_hypothesis = 85
mod_lit_premise = mod_lit_hypothesis = 80

# the hypothesis talks about the average marks obtained by a student in the same subjects as in the premise
if geo_hist_gov_hypothesis <= geo_hist_gov_premise:
    # check if the score in Geography, History and Government in the hypothesis contradicts the estimate of more than 'geo_hist_gov_premise'
    label = "contradiction"
elif geo_hist_gov_hypothesis == geo_hist_gov_premise and art_hypothesis == art_premise and comp_sci_hypothesis == comp_sci_premise and lit_hypothesis == lit_premise and mod_lit_hypothesis == mod_lit_premise:
    # if all the marks in the hypothesis exactly match the ones in the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the mark in Geography, History and Government
    # any mark greater than 'geo_hist_gov_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

