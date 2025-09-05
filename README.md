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
   python3 /nfshome0/atahmad/detconfig_parser/detconfig_parser.py 159 160 161
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
---+++ Layer 1
| *detector component* | *ROCs* | *159* | *160* |
| BPix_BmO_SEC5_LYR1_LDR4H_MOD2 | 8:11 | x |   |
| BPix_BpI_SEC6_LYR1_LDR4F_MOD1 | 12:15 |   | x |
```
