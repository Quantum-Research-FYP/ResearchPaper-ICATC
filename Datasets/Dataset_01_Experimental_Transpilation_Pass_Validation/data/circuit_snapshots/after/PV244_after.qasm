OPENQASM 3.0;
include "stdgates.inc";
qubit[6] q;
rx(0.3) q[0];
ry(0.5) q[0];
rz(0.7) q[0];
rx(0.2) q[1];
ry(0.4) q[1];
