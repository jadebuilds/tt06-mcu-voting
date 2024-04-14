# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_all_ones(dut):
  dut._log.info("Start")
  
  dut.ui_in.value = 0b11111111
  
  await ClockCycles(dut.clk, 1)

  assert dut.uo_out.value == 0b00000001
