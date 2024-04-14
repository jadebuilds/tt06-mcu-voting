![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/test/badge.svg)

# Voting for microcontroller redundancy

This is a fun lil first pass at a modified-consensus voting chip for .

It really ought to include dual-redundant signal paths but probably won't.

## Why does this matter?

Achieving [functional safety](https://en.wikipedia.org/wiki/Functional_safety) 
requires being tolerant of individual hardware failures. The simplest way to 
achieve this is redundancy -- e.g. running your control algorithm on
multiple microcontrollers such that even if one of them fails the algorithm
keeps running. Normally you might just "or" the outputs together; this chip
is us playing at a slightly more complicated / customizable means of combining
outputs from multiple processors.

## How it works

Inputs and outputs are digital signals (booleans). The output is a boolean also.
In the case of disagreement, an additional "default" / failsafe value is provided
as an input that the system can fall back on.