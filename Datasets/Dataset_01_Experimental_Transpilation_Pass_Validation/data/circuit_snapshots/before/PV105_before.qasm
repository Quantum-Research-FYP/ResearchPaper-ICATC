OPENQASM 3.0;
include "stdgates.inc";
qubit[3] q;
h q[0];
x q[1];
ccx q[0], q[1], q[2];
h q[2];
