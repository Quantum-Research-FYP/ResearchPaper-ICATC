OPENQASM 3.0;
include "stdgates.inc";
input float[64] theta;
qubit[6] q;
rx(theta) q[0];
rx(theta) q[0];
ry(theta) q[1];
ry(theta) q[1];
cx q[0], q[1];
