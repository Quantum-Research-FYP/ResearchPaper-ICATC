OPENQASM 3.0;
include "stdgates.inc";
qubit[7] q;
cx q[3], q[4];
h q[5];
cx q[5], q[6];
cx q[5], q[2];
swap q[2], q[5];
cx q[5], q[6];
