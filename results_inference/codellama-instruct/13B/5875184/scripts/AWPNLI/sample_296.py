premise_members = 5.0
premise_absent_members = 2.0
premise_points_per_member = 6.0

hypothesis_points = 18.0

# compute the total number of members who showed up
total_members = premise_members - premise_absent_members

# compute the total number of points scored by the members who showed up
total_points = total_members * premise_points_per_member

if total_points!= hypothesis_points:
    label = "contradiction"
else:
    label = "entailment"

print(label)
