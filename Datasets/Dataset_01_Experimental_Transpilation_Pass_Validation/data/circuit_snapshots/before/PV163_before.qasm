OPENQASM 3.0;
include "stdgates.inc";
input float[64] theta;
qubit[2] q;
ry(theta) q[0];
cx q[0], q[1];
rz(theta) q[1];
