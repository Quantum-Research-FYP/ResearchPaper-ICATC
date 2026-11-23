OPENQASM 3.0;
include "stdgates.inc";
qubit[3] q;
h q[0];
swap q[0], q[2];
cx q[2], q[1];
