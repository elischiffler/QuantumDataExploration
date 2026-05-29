# Homework 1 Written Responses

## Problem 1 – Infinite Square Well

![Problem 1 Plots](problem1_plots.pdf)

**How does the number of nodes relate to the quantum number $n$?**

A node is basically where the wave function crosses the x-axis. If you look at the graphs, $n=1$ has 0 nodes, $n=2$ has 1 node, and $n=3$ has 2 nodes. So, as the quantum number $n$ goes up, the number of nodes increases linearly. For any $n$, there are exactly $n-1$ nodes inside the well.

## Problem 2 - Energy Quantization

**Code Output**

--- First Three Allowed Energy Levels ---  
E_1 = 0.3764 eV  
E_2 = 1.5054 eV  
E_3 = 3.3872 eV  

--- Wavelength for Transition (n=3 -> n=1) ---  
Wavelength (λ) = 412.12 nm  

**Explain qualitatively why the energy levels become more widely separated as $n$ increases.**

In an infinite square well, a particle's energy scales quadratically with $n$ ($E_n \propto n^2$). If we look at the gap between any two adjacent levels ($\Delta E = E_{n+1} - E_n$), the difference scales like $(n+1)^2 - n^2 = 2n + 1$. Because $2n + 1$ grows as $n$ gets larger, the gap between the energy levels just keeps getting wider the higher you go.

## Problem 3 – Finite Well Bound States

**Code Output**

First bound-state energy: -9.7027 eV  
Second bound-state energy: -8.8151 eV  

![Problem 3 Plots](problem3_finite_well_states.pdf)

## Problem 4 – Infinite vs Finite Well Comparison

**Why are the energy levels of the finite well lower than those of the infinite well?**

In a finite well, the wave function isn't cut off instantly at the edges—it kind of "leaks" out a bit. Because the wave spreads out more, its effective width is larger. Since energy is inversely related to the width squared ($E \propto 1/L^2$), spreading out lowers the particle's energy. So, the finite well ends up with lower energy levels than the infinite well.

**Why does tunneling occur in the finite well but not in the infinite well?**

Tunneling happens when a particle has a chance of showing up outside the well, even if it classically doesn't have enough energy to break out. In an infinite well, the walls are literally impossible to get past (since it would require infinite energy), so the probability drops to exactly zero at the boundaries. But in our finite well, the walls are only 10 eV high. The wave function decays exponentially but doesn't instantly hit zero, which means there's a small but real chance the particle tunnels through.

**Compare the shapes of the wave functions near the boundaries.**

For the infinite well, the wave functions just crash into the walls and abruptly go to zero, making a sharp corner. But for the finite well, the transition is a lot smoother. The wave transitions cleanly from a standard wave inside the well to an exponentially decaying curve outside.

**Which system more closely resembles real physical systems? Explain.**

The finite well is definitely closer to reality. In the real world, nothing has "infinite" energy or infinite walls. It always takes some specific amount of energy to break a particle free. For example, knocking an electron out of a hydrogen atom takes exactly 13.6 eV. It's not trapped forever, which perfectly matches how our finite well model behaves.

---

## Problem 5 – Reflection

Basically, quantization means a trapped particle can't just have any random energy value. Its possible energy values can only be at certain values as energy can only be transferred in packets. This happens because of boundary conditions. When we force the wave function to be zero at the walls, we're basically creating standing waves. Only waves with specific wavelengths and energies fit perfectly inside the well without breaking those boundary rules.
