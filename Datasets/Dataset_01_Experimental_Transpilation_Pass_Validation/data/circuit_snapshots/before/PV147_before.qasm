OPENQASM 3.0;
include "stdgates.inc";
qubit[6] q;
h q[1];
cx q[1], q[2];
cx q[1], q[0];
swap q[0], q[1];
cx q[1], q[2];
cx q[4], q[5];
