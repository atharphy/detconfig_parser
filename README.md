# detconfig_parser

A utility script to parse CMS Pixel `detconfig` files and produce TWiki-style tables showing disabled ROCs across runs.

## Usage

1. SSH into the CMS user node:
   ```bash
   ssh username@cmsusr
   ```

2. From there, SSH into the server:
   ```bash
   ssh srv-s2b18-31-01
   ```

3. The `detconfig` files are located under:
   ```
   /pixelscratch/pixelscratch/config/Pix/detconfig
   ```

4. Run the parser by specifying the run numbers you want to compare:
   ```bash
   python3 /nfshome0/pixelpro/opstools/scripts/detconfig_parser.py 159 160 161
   ```

   - This will print the parsed tables to your terminal.
   - To save the output into a text file, use the `-o` option:
     ```bash
     python3 /nfshome0/atahmad/detconfig_parser/detconfig_parser.py 159 160 -o output.txt
     ```

## Output

- A timestamp table at the top showing when each `detectconfig.dat` file was created.
- Separate sections for **Layer 1–4** and **Ring 1–2**.
- Each detector component with its disabled ROC ranges.
- Columns mark which runs had those ROCs disabled.
- This output can directly be copied to the TWiki to make the exact same formatted tables.

Example table excerpt:

```
---+++ detconfig timestamps
| *159* | 2025-03-18 14:19:38 |
| *160* | 2025-04-01 11:22:38 |
| *161* | 2025-06-06 18:19:09 |

---+++ Layer 1
| *detector component* | *ROCs* | *159* | *160* | *161* |
| BPix_BmO_SEC5_LYR1_LDR4H_MOD2 | 8:11 | x | x | x |
| BPix_BpI_SEC1_LYR1_LDR1F_MOD3 | 12:15 | x | x | x |
| BPix_BpI_SEC5_LYR1_LDR4F_MOD4 | 12:15 | x | x | x |
| BPix_BpI_SEC6_LYR1_LDR4F_MOD1 | 12:15 |   | x | x |
| BPix_BpO_SEC4_LYR1_LDR3F_MOD3 | 0:3 | x | x | x |

---+++ Layer 2
| *detector component* | *ROCs* | *159* | *160* | *161* |
| BPix_BmI_SEC2_LYR2_LDR3F_MOD3 | 0:7 | x | x | x |
| BPix_BmI_SEC3_LYR2_LDR5F_MOD2 | 0:15 | x | x | x |
| BPix_BmI_SEC3_LYR2_LDR5F_MOD3 | 0:15 | x | x | x |
| BPix_BmI_SEC4_LYR2_LDR7F_MOD1 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR2_LDR11F_MOD4 | 0:15 | x | x | x |
| BPix_BmO_SEC1_LYR2_LDR2F_MOD1 | 0:15 | x | x | x |
| BPix_BmO_SEC3_LYR2_LDR5F_MOD3 | 0:15 | x | x | x |
| BPix_BmO_SEC5_LYR2_LDR8F_MOD1 | 0:15 |   |   | x |
| BPix_BmO_SEC5_LYR2_LDR8F_MOD2 | 0:15 | x | x | x |
| BPix_BmO_SEC8_LYR2_LDR14F_MOD2 | 0:7 | x | x | x |
| BPix_BpI_SEC2_LYR2_LDR3F_MOD4 | 0:15 | x | x | x |
| BPix_BpI_SEC7_LYR2_LDR11F_MOD2 | 8:15 | x | x | x |

---+++ Layer 3
| *detector component* | *ROCs* | *159* | *160* | *161* |
| BPix_BmI_SEC2_LYR3_LDR3F_MOD4 | 0:15 | x | x | x |
| BPix_BmI_SEC3_LYR3_LDR8F_MOD1 | 0:15 | x | x | x |
| BPix_BmI_SEC6_LYR3_LDR16F_MOD2 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR3_LDR18F_MOD1 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR3_LDR18F_MOD2 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR3_LDR18F_MOD3 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR3_LDR18F_MOD4 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR3_LDR19F_MOD1 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR3_LDR19F_MOD2 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR3_LDR19F_MOD3 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR3_LDR19F_MOD4 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR3_LDR20F_MOD1 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR3_LDR20F_MOD2 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR3_LDR20F_MOD3 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR3_LDR20F_MOD4 | 0:15 | x | x | x |
| BPix_BpI_SEC4_LYR3_LDR9F_MOD2 | 0:15 | x | x | x |
| BPix_BpI_SEC7_LYR3_LDR18F_MOD3 | 0:15 | x | x | x |

---+++ Layer 4
| *detector component* | *ROCs* | *159* | *160* | *161* |
| BPix_BmI_SEC3_LYR4_LDR10F_MOD2 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR25F_MOD1 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR25F_MOD2 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR25F_MOD3 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR25F_MOD4 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR26F_MOD1 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR26F_MOD2 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR26F_MOD3 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR26F_MOD4 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR27F_MOD1 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR27F_MOD2 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR27F_MOD3 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR27F_MOD4 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR28F_MOD1 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR28F_MOD2 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR28F_MOD3 | 0:15 | x | x | x |
| BPix_BmI_SEC7_LYR4_LDR28F_MOD4 | 0:15 | x | x | x |
| BPix_BmO_SEC6_LYR4_LDR23F_MOD2 | 0:15 | x | x | x |
| BPix_BmO_SEC7_LYR4_LDR27F_MOD4 | 0:15 | x | x | x |
| BPix_BpI_SEC5_LYR4_LDR18F_MOD4 | 0:15 | x | x | x |

---+++ Ring 1
| *detector component* | *ROCs* | *159* | *160* | *161* |
| FPix_BmI_D1_BLD6_PNL1_RNG1 | 0:15 | x | x | x |
| FPix_BmO_D1_BLD4_PNL1_RNG1 | 0:15 | x | x | x |
| FPix_BmO_D1_BLD4_PNL2_RNG1 | 0:15 | x | x | x |
| FPix_BmO_D1_BLD5_PNL1_RNG1 | 0:15 | x | x | x |
| FPix_BmO_D1_BLD5_PNL2_RNG1 | 0:15 | x | x | x |
| FPix_BmO_D1_BLD6_PNL1_RNG1 | 0:15 | x | x | x |
| FPix_BmO_D1_BLD6_PNL2_RNG1 | 0:15 | x | x | x |
| FPix_BpI_D1_BLD4_PNL2_RNG1 | 0:15 | x | x | x |
| FPix_BpI_D1_BLD7_PNL1_RNG1 | 0:15 | x | x | x |
| FPix_BpO_D1_BLD10_PNL1_RNG1 | 0:15 | x | x | x |
| FPix_BpO_D2_BLD4_PNL1_RNG1 | 0:15 | x | x | x |
| FPix_BpO_D3_BLD9_PNL2_RNG1 | 0:15 | x | x | x |

---+++ Ring 2
| *detector component* | *ROCs* | *159* | *160* | *161* |
| FPix_BmI_D3_BLD1_PNL2_RNG2 | 8:15 | x | x | x |
| FPix_BmO_D1_BLD5_PNL1_RNG2 | 0:15 | x | x | x |
| FPix_BmO_D1_BLD5_PNL2_RNG2 | 0:15 | x | x | x |
| FPix_BmO_D1_BLD6_PNL1_RNG2 | 0:15 | x | x | x |
| FPix_BmO_D1_BLD6_PNL2_RNG2 | 0:15 | x | x | x |
| FPix_BmO_D1_BLD7_PNL1_RNG2 | 0:15 | x | x | x |
| FPix_BmO_D1_BLD7_PNL2_RNG2 | 0:15 | x | x | x |
| FPix_BmO_D1_BLD8_PNL1_RNG2 | 0:15 | x | x | x |
| FPix_BmO_D1_BLD8_PNL2_RNG2 | 0:15 | x | x | x |
| FPix_BmO_D2_BLD2_PNL1_RNG2 | 0:15 | x | x | x |
| FPix_BpI_D1_BLD17_PNL1_RNG2 | 0:15 | x | x | x |
| FPix_BpI_D2_BLD4_PNL1_RNG2 | 0:15 | x | x | x |
| FPix_BpI_D3_BLD14_PNL1_RNG2 | 0:15 | x | x | x |
| FPix_BpI_D3_BLD15_PNL1_RNG2 | 0:15 | x | x | x |
| FPix_BpI_D3_BLD16_PNL1_RNG2 | 0:15 | x | x | x |
| FPix_BpI_D3_BLD17_PNL1_RNG2 | 0:15 | x | x | x |
| FPix_BpI_D3_BLD1_PNL2_RNG2 | 0:7 | x | x | x |
```
