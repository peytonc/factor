Research an efficient algorithm to navigate the Berggren tree of Primitive Pythagorean Triples (PPT) and find the non-trivial path to the node containing a_target. The PPT can only be exhaustively searched to a limited depth. Search for a specific node in the PPT tree where the first coordinate a_target equals a known, odd, semiprime integer whose factors are unknown. Only a limited shallow tree search can be performed because a_target's tree depth is extremely large.

Global Definitions:
Let m = (q+p)/2 = (sqrt(c+b)+sqrt(c-b))/2 be a Euclid formula parameter.
Let n = (q-p)/2 = (sqrt(c+b)-sqrt(c-b))/2, with m>n>0 and gcd(m,n)=1, be a Euclid formula parameter.
Let p = m − n = sqrt(c-b) and is the smaller factor of a.
Let q = m + n = sqrt(c+b) and is the larger factor of a, with 1<p<q.
Let a = m^2 − n^2 = p*q and is the odd leg.
Let b = 2mn = (q^2 - p^2)/2 and is the even leg.
Let c = m^2 + n^2 = (p^2 + q^2)/2 and is the hypotenuse.
Let a_target = large known odd semiprime integer (representing the odd leg a).
Let m_target, n_target, p_target, and q_target be the non-trivial integers whose values are unknown.
Let Berggren_A = [ [ 1, -2, 2 ], [ 2, -1, 2 ], [ 2, -2, 3 ] ].
Let Berggren_B = [ [ 1, 2, 2 ], [ 2, 1, 2 ], [ 2, 2, 3 ] ].
Let Berggren_C = [ [ -1, 2, 2 ], [ -2, 1, 2 ], [ -2, 2, 3 ] ].
Let A = [ [ 1, 0, 0 ], [ 4, 1, 4 ], [ 2, 0, 1 ] ] be the factor state matrix corresponding to Berggren_A.
Let B = [ [ 0, 1, 0 ], [ 1, 4, 4 ], [ 0, 2, 1 ] ] be the factor state matrix corresponding to Berggren_B.
Let C = [ [ 0, 1, 0 ], [ 1, 4, -4 ], [ 0, 2, -1 ] ] be the factor state matrix corresponding to Berggren_C.
Let G ∈ {A​, B​, C​} be a selected generator in the set of state transition matrices.
Let v_root = [1, 9, 3]^T be the root of the projected PPT tree.
Let v = [p^2, q^2, a]^T ∈ ℤ^3 be the algebraic state vector of a PPT node.
Let P = G_1 * G_2 * ... * G_d, where G_i ∈ { A, B, C }, be a sequence of generators applied to the root v_root to reach depth d.
