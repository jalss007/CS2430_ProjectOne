# Project Plan & Progress Log

## Team Structure & Role Assignments
- **Implementation Lead:** Alain
- **Verification Lead:** Jose
- **Communications Lead:** Kosoma

---

## Milestone Checklist

- [x] **Task 1: Repository Setup & Workflow**
  - **Status:** Done
  - **Assigned To:** Jose
  - **Evidence:** GitHub repository initialized + UML diagram template created

- [x] **Task 2: Lexicographic Permutation Generator (`next_permutation`)**
  - **Status:** Done
  - **Assigned To:** Alain / Kosoma
  - **Evidence:** `src/permutations.py` (`next_permutation` and `permutations` functions)

- [ ] **Task 3: Sorting Algorithms Implementation & Comparison Counter**
  - **Status:** In Progress
  - **Assigned To:** Team
  - **Evidence:** Branch `feature/sorting-algos`

- [x] **Task 4: UML & System Structure Diagram**
  - **Status:** Done (Scheduled for Saturday)
  - **Assigned To:** Team

- [ ] **Task 5: Part 3 Test Driver & Data Collection ($n = 4, 6, 8$)**
  - **Status:** To Do
  - **Assigned To:** Team

---

## Weekly Status Log

### Week 1 Status Report

**Who did you help this week?**
Helped Alain integrate and test the pivot finding and suffix reversal logic with the swap steps in `next_permutation()`.

**Who helped you this week?**
- **Jose:** Set up the shared GitHub repository and initialized the UML diagram template for our team meeting.
- **Alain:** Implemented the pivot-finding loop (`k`) and suffix reversal logic in `next_permutation()`.

**What did you do this week?**
- Implemented the search for swap index `l` and element swap inside `next_permutation()`.
- Debugged slice syntax error in `reversed(i[k + 1:])` to ensure full array traversal works properly.
- Implemented the generator function `permutations(n)` yielding tuple snapshots of state.
- **Evidence Pointers:** File path `src/permutations.py` (`next_permutation` and `permutations` functions).

**What are you planning to do next week?**
- Finalize the UML diagram design with Jose and Alain during our Saturday meeting.
- Begin integrating `permutations(n)` into the Part 3 Test Driver (`main.py`) to start capturing comparison counts for Mergesort, Quicksort, Shaker sort, and Heapsort.

**Blocker / risk this week?**
None. Resolved the slice index syntax bug in `next_permutation()`.

### Week 2 Status Report
