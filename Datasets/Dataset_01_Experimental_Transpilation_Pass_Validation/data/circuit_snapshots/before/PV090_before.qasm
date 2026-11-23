OPENQASM 3.0;
include "stdgates.inc";
qubit[6] q;
cx q[2], q[3];
cx q[3], q[4];
swap q[2], q[3];
cx q[3], q[4];
