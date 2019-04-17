# Tasks

#################################---------simple_relabeling---------#########################################
# Rules - 1, 2
#################################---------complex_relabeling---------#########################################
# Rules
#################################---------reordering---------#########################################
# Rules
#################################---------deletion---------###########################################
# Rules - 8, 9, 10


# Rule 1
# Pass State 
for i in range(2,250,10):
	print("- state: q")
	print("  lhs: '(",i," ?x0 ?x1)'")
	print("  rhs: '(",i," ?x0 ?x1)'")
	print("  newstates:")
	print("  - [[0], q]")
	print("  - [[1], q]")
	print("  weight: 1.0")

# Rule 2
# Pass State and relabel Head
for i in range(1,250,2):
	print("- state: q")
	print("  lhs: '(",i," ?x0 ?x1)'")
	print("  rhs: '(",i+1," ?x0 ?x1)'")
	print("  newstates:")
	print("  - [[0], q]")
	print("  - [[1], q]")
	print("  weight: 1.0")

# Rule 3
# Swap L and R
for i in range(2,250,10):
	print("- state: q")
	print("  lhs: '(",i," ?x0 ?x1)'")
	print("  rhs: '(",i," ?x1 ?x0)'")
	print("  newstates:")
	print("  - [[0], q]")
	print("  - [[1], q]")
	print("  weight: 1.0")

# Rule 4
# Insert j to the left
for i in range(3,250,10):
	for j in range(3, 250, 30):
		print("- state: q")
		print("  lhs: '(",i," ?x0 ?x1)'")
		print("  rhs: '(",i," (",j" ?x0) ?xi)'")
		print("  newstates:")
		print("  - [[0, 0], q]")
		print("  - [[1], q]")
		print("  weight: 1.0")

# Rule 5
# Insert j to the right
for i in range(1,250,10):
	for j in range(3, 250, 30):
		print("- state: q")
		print("  lhs: '(",i," ?x0 ?x1)'")
		print("  rhs: '(",i," ?x0 (",j" ?x1))'")
		print("  newstates:")
		print("  - [[0, 0], q]")
		print("  - [[1], q]")
		print("  weight: 1.0")

# Rule 6
# Insert j below
for i in range(1,250,10):
	for j in range(3, 250, 30):
		print("- state: q")
		print("  lhs: '(",i," ?x0 ?x1)'")
		print("  rhs: '(",i," (",j" ?x0 ?xi))'")
		print("  newstates:")
		print("  - [[0, 0], q]")
		print("  - [[1], q]")
		print("  weight: 1.0")

# Rule 7
# Delete head->head+10
for i in range(1,250,4):
	print("- state: q")
	print("  lhs: '(",i," ?x0 ?x1)'")
	print("  rhs: '",i+10,"'")
	print("  weight: 1.0")

# Rule 8
# Delete head->head*20
for i in range(2,250,4):
	print("- state: q")
	print("  lhs: '(",i," ?x0 ?x1)'")
	print("  rhs: '",i*20,"'")
	print("  weight: 1.0")

# Rule 9
# Delete Right Subtree
for i in range(3,250,4):
	print("- state: q")
	print("  lhs: '(",i," ?x0 ?x1)'")
	print("  rhs: '(",i," ?x0)'")
	print("  weight: 1.0")

# Rule 10
# Delete Left Subtree
for i in range(4,250,4):
	print("- state: q")
	print("  lhs: '(",i," ?x0 ?x1)'")
	print("  rhs: '(",i," ?x1)'")
	print("  weight: 1.0")



