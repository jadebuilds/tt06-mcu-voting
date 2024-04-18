/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`define default_netname none

module tt_um_voting_thingey (
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
  // note: 0 == safe; 1 == 
  wire voter0 = ui_in[0];
  wire voter1 = ui_in[1];
  wire voter2 = ui_in[2];
  wire voter3 = ui_in[3];
  wire voter4 = ui_in[4];
  wire voter5 = ui_in[5];
  wire voter6 = ui_in[6];
  wire voter7 = ui_in[7];

  wire[3:0] num_voters = uio_in[3:0]; // 4 bits for voters 0000 -> 1111
  wire[2:0] num_fails_okay = uio_in[6:4];  // 0 by default // 3 bits - max of 7 

  // depending on the voters: count failures
  // num voters =?= 5 => ui_in[first five]
  reg[3:0] count_fails = 0;  
  reg result;
  always @* begin
    count_fails = 0;  // Reset count_fails each time
    for (int i = 0; i < 8; i++) begin
      if (i < num_voters) begin
        count_fails += ui_in[i];
      end
    end
    result = (count_fails > num_fails_okay);
  end

  // compute result based on threshold and voters 
  // assign result = voter0 | voter1 | voter2 | voter3 | voter4 | voter5 | voter6 | voter7;
  
  assign uo_out[4:1] = count_fails;
  assign uo_out[0] = result;

  // All output pins must be assigned. If not used, assign to 0.
  assign uo_out[7:5]  = 0;  // Remainder assigned low
  assign uio_out = 0;
  assign uio_oe  = 0;

endmodule
