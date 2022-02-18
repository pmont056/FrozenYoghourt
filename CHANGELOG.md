Change Log

==========

0.0.1 (10/02/2022)
------------------
- First Release

Date: 10/2/2022

1. Wrote README file
2. Add P gates method to gates.py
3. Add CU method to gates.py
4. Add view method to mode.py
5. Add log.txt for keeping track of changes

0.0.3 (11/02/2022)
------------------

1. Move to_su to maths.py
2. Move kron_decomp to quantum.py
3. Change default variable in the chi method to "x"

0.0.7 (12/02/2022)
------------------

1. Import gates.py to quantum.py

0.0.8 (12/02/2022)
------------------

1. Fix Quantum.double_cosets by importing the correct packages
2. Add default_import method to allow for faster import prompt
3. Change random_local_gates to random_local_ops and allow for creating more operation at the same time.
4. Allow for doing to_su on list of matrices.

0.0.10.1 (15/02/2022)
-------------------

1. Add view method to visualize numerical matrices
2. Add CAN method
3. Add Gamma gates

0.0.11 (17/02/2022)
-------------------

1. Delete Class from files so now g.CAN will just be CAN. Although the Mode class is kept.
2. Fix default_import to match the change in 1.

0.0.12 (17/02/2022)
-------------------

1. Allow for custom custom mode toggle
2. Add color to toggle / now

0.0.12.2 (17/02/2022)
---------------------

1. Add a dagger function that can operate on multiple matrices input
2. Fix the to_su function so that it can operate on multiple matrices input
3. Delete double_cosets to be replaced with the KAK
4. Add printing parameter to toggle to allow for not printing results


0.0.13 (18/02/2022)
-------------------

1. Change P gate to Phase
2. Change chi to include coefficients return of symbolic matrices.
3. Change random_local_ops to local_ops
4. Replace U function with u2 function which now allows for special unitary gates
5. Fix local_ops so that it nows includes a special unitary option
6. Add evaluate numerical returns for to_su
7. Add canonical_class_vector method