/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`define default_netname none

module tt_um_example (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // will go high when the design is enabled
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  // some processing! 
  // all the input becomes a part of our voting system 
  assign wire voter0 = ui_in[0];
  assign wire voter1 = ui_in[1];
  assign wire voter2 = ui_in[2];
  assign wire voter3 = ui_in[3];
  assign wire voter4 = ui_in[4];
  assign wire voter5 = ui_in[5];
  assign wire voter6 = ui_in[6];
  assign wire voter7 = ui_in[7];

  // then we do a an "or" and assign to the first register of the output
  assign uo_out[0] = voter0 | voter1 | voter2 | voter3 | voter4 | voter5 | voter6 | voter7;

  // All output pins must be assigned. If not used, assign to 0.
  assign uo_out[7:1]  = 0;  // Example: ou_out is the sum of ui_in and uio_in
  assign uio_out = 0;
  assign uio_oe  = 0;

endmodule
