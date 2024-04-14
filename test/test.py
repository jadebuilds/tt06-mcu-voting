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
  dut.uio_in.value = 0
  dut.rst_n.value = 0
  await ClockCycles(dut.clk, 10)
  dut.rst_n.value = 1

  # Yea why not let's see some clock cycles in the .tcd 

  # Set the input values, wait one clock cycle, and check the output
  dut._log.info("Test")
  dut.ui_in.value = 20
  dut.uio_in.value = 30

  await ClockCycles(dut.clk, 1)

  assert dut.uo_out.value == 50
