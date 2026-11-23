OPENQASM 3.0;
include "stdgates.inc";
qubit[7] q;
cx q[1], q[2];
cx q[2], q[3];
swap q[1], q[2];
cx q[2], q[3];
