OPENQASM 3.0;
include "stdgates.inc";
qubit[7] q;
h q[0];
swap q[0], q[1];
cx q[1], q[2];
