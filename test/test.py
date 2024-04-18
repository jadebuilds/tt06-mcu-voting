# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
  dut._log.info("Start")
  
  # We don't use the clock currently but we're gonna invoke it anyway just in case
  clock = Clock(dut.clk, 10, units="us")
  cocotb.start_soon(clock.start())

  # We don't really use these either??? but who knows
  dut._log.info("Reset")
  dut.ena.value = 1
  dut.ui_in.value = 0
  dut.uio_in.value = 0b00001000  # [3:0] encodes 8 voters
  dut.rst_n.value = 0
  await ClockCycles(dut.clk, 10)
  dut.rst_n.value = 1

  dut._log.info("Test case: Given all 1 input, should emit 1 (N-0 consensus, 8 voters)")  

  # Set the input values, wait one clock cycle, and check the output
  dut.ui_in.value = 0b11111111

  await ClockCycles(dut.clk, 1)

  assert dut.uo_out.value & 0b00000001 == 1  # result
  assert (dut.uo_out.value & 0b00011110) >> 1 == 8  # num_failed

  dut._log.info("Test case: Given any 1 input, should emit 1")  

  # Set the input values, wait one clock cycle, and check the output
  dut.ui_in.value = 0b00000100

  await ClockCycles(dut.clk, 1)

  assert dut.uo_out.value & 0b00000001 == 1  # result
  assert (dut.uo_out.value & 0b00011110) >> 1 == 1  # num_failed

  dut._log.info("Test case: Given all 0 input, should emit 0")

  # Set the input values, wait one clock cycle, and check the output
  dut.ui_in.value = 0b00000000

  await ClockCycles(dut.clk, 1)

  assert dut.uo_out.value & 0b00000001 == 0  # result
  assert (dut.uo_out.value & 0b00011110) >> 1 == 0  # num_failed

  dut._log.info("Test case: Given N-1 consensus on 8 voters, should emit 0 with a single 1 input")

  dut.uio_in.value = (1 << 4) | (8 << 0)  # [3:0]=8 means 8 voters, [6:4]=1 means N-1 consensus
  dut.ui_in.value = 0b00000100

  await ClockCycles(dut.clk, 1)

  assert dut.uo_out.value & 0b00000001 == 0  # result
  assert (dut.uo_out.value & 0b00011110) >> 1 == 1  # num_failed

  dut._log.info("Test case: Given 5 voters, should ignore the other votes")

  dut.uio_in.value = (0 << 4) | (5 << 0)  # [3:0]=5 means 5 voters, [6:4]=0 means N-0 consensus
  dut.ui_in.value = 0b11100000

  await ClockCycles(dut.clk, 1)

  assert dut.uo_out.value & 0b00000001 == 0  # result
  assert (dut.uo_out.value & 0b00011110) >> 1 == 0  # num_failed

