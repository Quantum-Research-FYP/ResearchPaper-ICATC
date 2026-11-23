OPENQASM 3.0;
include "stdgates.inc";
qubit[2] q;
crx(0.5) q[0], q[1];
cry(0.7) q[0], q[1];
crz(0.9) q[0], q[1];
