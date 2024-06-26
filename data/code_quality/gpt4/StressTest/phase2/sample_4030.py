total_notes_premise = 300
total_notes_hypothesis = 100

# The hypothesis talks about the total number of currency notes Gokul had, which is also mentioned in the premise
if total_notes_hypothesis >= total_notes_premise:
    # Check if the total number of notes in the hypothesis contradicts the premise of having less than 'total_notes_premise'
    label = "contradiction"
elif total_notes_hypothesis < total_notes_premise:
    # The premise gives only an estimate (less than 'total_notes_premise') for the total number of notes
    # A number of notes less than 'total_notes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
