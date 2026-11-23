# Complete 20-Item Assessment Instrument (Pre-Test & Post-Test)

This document contains the full text, multiple-choice options (A–D), and correct answer keys for the 20 questions administered to participants in **Group A (Platform)** and **Group B (Comparison)**.

The pre-test and post-test use **isomorphic items** covering identical core competencies and difficulty levels to ensure fair pre/post learning gain comparison.

---

## Topic 1: Circuit Construction (Items 1–5)

### Item 01
* **Pre-Test (PRE_01):** What is a qubit?
  * [ ] A: A classical bit that can only store 0
  * [ ] B: A classical bit that can only store 1
  * [x] **C: A basic unit of quantum information (Correct)**
  * [ ] D: A type of quantum gate
* **Post-Test (POST_01):** Which of the following best describes a qubit?
  * [ ] A: A physical wire that carries classical data
  * [x] **B: The basic unit of quantum information (Correct)**
  * [ ] C: A quantum measurement result
  * [ ] D: A quantum compiler

---

### Item 02
* **Pre-Test (PRE_02):** What are the two computational basis states of a qubit?
  * [ ] A: $|+\rangle$ and $|-\rangle$
  * [x] **B: $|0\rangle$ and $|1\rangle$ (Correct)**
  * [ ] C: $|00\rangle$ and $|11\rangle$
  * [ ] D: $|H\rangle$ and $|X\rangle$
* **Post-Test (POST_02):** Which pair represents the standard computational basis states of one qubit?
  * [x] **A: $|0\rangle$ and $|1\rangle$ (Correct)**
  * [ ] B: $|+\rangle$ and $|-\rangle$
  * [ ] C: $|00\rangle$ and $|01\rangle$
  * [ ] D: $H$ and $X$

---

### Item 03
* **Pre-Test (PRE_03):** What is the main purpose of a quantum gate?
  * [ ] A: To store a quantum circuit
  * [x] **B: To perform an operation on one or more qubits (Correct)**
  * [ ] C: To convert a qubit into a classical bit
  * [ ] D: To connect a quantum computer to the internet
* **Post-Test (POST_03):** What does applying a quantum gate generally do?
  * [x] **A: Performs a mathematical operation on one or more qubits (Correct)**
  * [ ] B: Automatically measures every qubit
  * [ ] C: Increases the number of physical qubits
  * [ ] D: Converts quantum information directly into classical information

---

### Item 04
* **Pre-Test (PRE_04):** What does a measurement operation do to a qubit?
  * [ ] A: Always changes it to $|1\rangle$
  * [x] **B: Produces a classical measurement result (Correct)**
  * [ ] C: Deletes the qubit
  * [ ] D: Creates another qubit
* **Post-Test (POST_04):** What is obtained when a qubit is measured?
  * [x] **A: A classical result (Correct)**
  * [ ] B: Another qubit
  * [ ] C: A new quantum gate
  * [ ] D: A coupling map

---

### Item 05
* **Pre-Test (PRE_05):** Which gate is commonly used to create a superposition from $|0\rangle$?
  * [ ] A: $X$
  * [ ] B: $Z$
  * [x] **C: $H$ (Correct)**
  * [ ] D: $\text{SWAP}$
* **Post-Test (POST_05):** Which gate is commonly used to place a qubit initially in $|0\rangle$ into an equal superposition?
  * [ ] A: $\text{SWAP}$
  * [ ] B: $X$
  * [x] **C: $H$ (Correct)**
  * [ ] D: $CZ$

---

## Topic 2: Superposition and Entanglement (Items 6–10)

### Item 06
* **Pre-Test (PRE_06):** What does the $X$ gate do to $|0\rangle$?
  * [x] **A: Changes it to $|1\rangle$ (Correct)**
  * [ ] B: Changes it to $|+\rangle$
  * [ ] C: Leaves it unchanged
  * [ ] D: Measures it
* **Post-Test (POST_06):** If an $X$ gate is applied to $|1\rangle$, what is the resulting state?
  * [x] **A: $|0\rangle$ (Correct)**
  * [ ] B: $|1\rangle$
  * [ ] C: $|+\rangle$
  * [ ] D: $|-\rangle$

---

### Item 07
* **Pre-Test (PRE_07):** A quantum circuit contains three qubit wires. How many qubits does it operate on?
  * [ ] A: 1
  * [ ] B: 2
  * [x] **C: 3 (Correct)**
  * [ ] D: 6
* **Post-Test (POST_07):** A circuit has five quantum wires. How many qubits does the circuit contain?
  * [ ] A: 2
  * [ ] B: 3
  * [x] **C: 5 (Correct)**
  * [ ] D: 10

---

### Item 08
* **Pre-Test (PRE_08):** What does a two-qubit gate operate on?
  * [ ] A: Only one qubit
  * [x] **B: Two qubits (Correct)**
  * [ ] C: Three qubits
  * [ ] D: A classical bit and a qubit
* **Post-Test (POST_08):** A $CX$ gate is an example of:
  * [ ] A: A one-qubit gate
  * [x] **B: A two-qubit gate (Correct)**
  * [ ] C: A measurement operation
  * [ ] D: A classical operation

---

### Item 09
* **Pre-Test (PRE_09):** What state results from applying an $H$ gate to $|0\rangle$?
  * [ ] A: $|0\rangle$
  * [ ] B: $|1\rangle$
  * [x] **C: $(|0\rangle + |1\rangle)/\sqrt{2}$ (Correct)**
  * [ ] D: $(|0\rangle - |1\rangle)/\sqrt{2}$
* **Post-Test (POST_09):** What is the ideal probability of measuring 1 after applying $H$ to a qubit initially in $|0\rangle$?
  * [ ] A: 0%
  * [ ] B: 25%
  * [x] **C: 50% (Correct)**
  * [ ] D: 100%

---

### Item 10
* **Pre-Test (PRE_10):** If a qubit is in an equal superposition of $|0\rangle$ and $|1\rangle$, what is the probability of measuring 0?
  * [ ] A: 0%
  * [ ] B: 25%
  * [x] **C: 50% (Correct)**
  * [ ] D: 100%
* **Post-Test (POST_10):** Which expression represents an equal superposition of $|0\rangle$ and $|1\rangle$?
  * [ ] A: $|0\rangle$
  * [ ] B: $|1\rangle$
  * [x] **C: $(|0\rangle + |1\rangle)/\sqrt{2}$ (Correct)**
  * [ ] D: $|0\rangle + |1\rangle$ (unnormalised)

---

## Topic 3: Transpilation and Routing (Items 11–14)

### Item 11
* **Pre-Test (PRE_11):** Which combination of gates can create the Bell state $(|00\rangle + |11\rangle)/\sqrt{2}$?
  * [ ] A: $X$ followed by $X$
  * [x] **B: $H$ on the first qubit followed by $CX$ (Correct)**
  * [ ] C: $Z$ followed by $\text{SWAP}$
  * [ ] D: $H$ on both qubits only
* **Post-Test (POST_11):** Starting with $|00\rangle$, which sequence creates an entangled Bell state?
  * [ ] A: $X$ on $q_0$, then $X$ on $q_1$
  * [x] **B: $H$ on $q_0$, then $CX(q_0, q_1)$ (Correct)**
  * [ ] C: $Z$ on $q_0$, then $Z$ on $q_1$
  * [ ] D: $\text{SWAP}(q_0, q_1)$

---

### Item 12
* **Pre-Test (PRE_12):** What is quantum entanglement?
  * [ ] A: Two classical bits having the same value
  * [x] **B: A relationship between quantum systems where their states are correlated in a quantum-mechanical way (Correct)**
  * [ ] C: A method for increasing the number of physical qubits
  * [ ] D: A technique for removing quantum noise
* **Post-Test (POST_12):** Which statement best describes entanglement?
  * [ ] A: Two qubits are simply stored next to each other
  * [x] **B: Quantum states of different systems can become strongly correlated (Correct)**
  * [ ] C: Two qubits must always have identical values
  * [ ] D: Entanglement removes all noise from a circuit

---

### Item 13
* **Pre-Test (PRE_13):** If a Bell state is $(|00\rangle + |11\rangle)/\sqrt{2}$, which measurement outcomes can ideally occur?
  * [ ] A: Only 00
  * [ ] B: Only 11
  * [x] **C: 00 and 11 (Correct)**
  * [ ] D: 01 and 10
* **Post-Test (POST_13):** A circuit prepares $(|00\rangle + |11\rangle)/\sqrt{2}$. Which set contains all possible ideal measurement outcomes?
  * [ ] A: $\{00\}$
  * [ ] B: $\{11\}$
  * [x] **C: $\{00, 11\}$ (Correct)**
  * [ ] D: $\{01, 10\}$

---

### Item 14
* **Pre-Test (PRE_14):** What is quantum circuit transpilation?
  * [x] **A: Converting a quantum circuit into a form suitable for a target quantum device (Correct)**
  * [ ] B: Measuring all qubits
  * [ ] C: Creating a quantum algorithm from scratch
  * [ ] D: Converting a quantum computer into a classical computer
* **Post-Test (POST_14):** What is the main purpose of a quantum transpiler?
  * [x] **A: To adapt a circuit to the requirements of a target quantum device (Correct)**
  * [ ] B: To teach quantum mechanics
  * [ ] C: To measure qubits
  * [ ] D: To create classical software

---

## Topic 4: Hardware Constraints (Items 15–17)

### Item 15
* **Pre-Test (PRE_15):** Why might a transpiler insert additional gates into a circuit?
  * [ ] A: To make the circuit look more complicated
  * [x] **B: To satisfy the target device's gate set or connectivity constraints (Correct)**
  * [ ] C: To increase the number of qubits
  * [ ] D: To change the algorithm's intended result
* **Post-Test (POST_15):** A circuit contains a two-qubit operation between two qubits that are not directly connected on the target hardware. What might the transpiler do?
  * [ ] A: Remove the operation
  * [x] **B: Insert routing operations such as SWAP gates (Correct)**
  * [ ] C: Delete one of the qubits
  * [ ] D: Stop the quantum computer permanently

---

### Item 16
* **Pre-Test (PRE_16):** What can happen to circuit depth after transpilation?
  * [ ] A: It can never change
  * [ ] B: It can only decrease
  * [x] **C: It can increase or decrease depending on the transformations (Correct)**
  * [ ] D: It always becomes zero
* **Post-Test (POST_16):** Which statement about transpilation is correct?
  * [ ] A: Transpilation always reduces circuit depth
  * [ ] B: Transpilation never changes the circuit
  * [x] **C: Transpilation can transform the circuit and may increase or decrease its depth (Correct)**
  * [ ] D: Transpilation only changes measurement results

---

### Item 17
* **Pre-Test (PRE_17):** Why can't every pair of physical qubits necessarily perform a two-qubit gate directly?
  * [x] **A: Physical qubits may have limited connectivity (Correct)**
  * [ ] B: Qubits only work in pairs
  * [ ] C: Quantum gates only work on classical bits
  * [ ] D: Two-qubit gates are not allowed on quantum computers
* **Post-Test (POST_17):** What does limited qubit connectivity mean?
  * [ ] A: Every qubit can interact directly with every other qubit
  * [x] **B: Only certain pairs of physical qubits can directly perform some two-qubit operations (Correct)**
  * [ ] C: Qubits cannot interact with each other
  * [ ] D: The computer has no physical qubits

---

## Topic 5: Optimization & Debugging (Items 18–20)

### Item 18
* **Pre-Test (PRE_18):** What is a coupling map?
  * [x] **A: A map showing the physical connectivity between qubits (Correct)**
  * [ ] B: A map of quantum algorithms
  * [ ] C: A list of measurement results
  * [ ] D: A map of software developers
* **Post-Test (POST_18):** What information does a coupling map primarily provide?
  * [x] **A: Which physical qubits can directly interact (Correct)**
  * [ ] B: The probability of measuring each qubit
  * [ ] C: The number of quantum algorithms installed
  * [ ] D: The number of students using the computer

---

### Item 19
* **Pre-Test (PRE_19):** What is one possible solution when two logical qubits need a two-qubit gate but their physical qubits are not directly connected?
  * [ ] A: Delete the gate
  * [x] **B: Insert routing operations such as SWAP gates (Correct)**
  * [ ] C: Turn off the quantum computer
  * [ ] D: Convert all qubits into classical bits
* **Post-Test (POST_19):** A logical $CX$ requires qubits mapped to physical qubits 0 and 3, but the hardware only connects 0-1-2-3 in a line. What may the compiler introduce?
  * [x] **A: Routing operations such as SWAPs (Correct)**
  * [ ] B: Additional classical computers
  * [ ] C: More measurement devices
  * [ ] D: Nothing; the $CX$ must always be removed

---

### Item 20
* **Pre-Test (PRE_20):** Circuit: $q_0 \text{ --H--*--}$, $q_1 \text{ -----X--}$ (a $CX$ with control $q_0$, target $q_1$ after an $H$ on $q_0$). What is the main purpose of the $CX$ gate?
  * [ ] A: To measure $q_0$
  * [x] **B: To create a correlation/entanglement between $q_0$ and $q_1$ (Correct)**
  * [ ] C: To delete $q_1$
  * [ ] D: To convert $q_0$ into a classical bit
* **Post-Test (POST_20):** A learner's circuit has a $CX$ (control $q_0$, target $q_1$), but the target hardware does not directly connect the physical qubits assigned to $q_0$ and $q_1$. What is the most likely reason the transpiled circuit contains additional SWAP gates?
  * [ ] A: The compiler is randomly changing the algorithm
  * [x] **B: The compiler is routing the qubits to satisfy hardware connectivity (Correct)**
  * [ ] C: The compiler is measuring the qubits
  * [ ] D: The compiler is removing the $CX$ operation

---

## Standard 10-Item Usability Questionnaire (SUS)
*(Administered on a 5-point Likert scale: 1 = Strongly Disagree to 5 = Strongly Agree)*

1. I think that I would like to use this platform frequently.
2. I found the platform unnecessarily complex.
3. I thought the platform was easy to use.
4. I think that I would need the support of a technical person to be able to use this platform.
5. I found the various functions in this platform were well integrated.
6. I thought there was too much inconsistency in this platform.
7. I would imagine that most people would learn to use this platform very quickly.
8. I found the platform very cumbersome to use.
9. I felt very confident using the platform.
10. I needed to learn a lot of things before I could get going with this platform.

---

## Platform Component & Transparency Ratings
*(Administered on a 5-point Likert scale: 1 = Strongly Disagree to 5 = Strongly Agree)*

* **Transparency:** "The step-by-step compilation (pass) view helped me understand what the compiler did to my circuit."
* **AI Algorithm Tutor:** "The AI tutor's answers were helpful for understanding my circuit."
* **Circuit Builder:** "The visual circuit builder was easy to use."
* **Multi-Framework IDE:** "The code view / IDE was easy to use."
* **Hardware Execution:** "Seeing the circuit run on real or simulated hardware helped me understand hardware constraints."
