OPENQASM 3.0;
include "stdgates.inc";
qubit[7] q;
h q[0];
cry(0.5) q[0], q[1];
cx q[1], q[2];
rz(0.3) q[2];
