import json
from pathlib import Path

# 1. Define the filename of your notebook
NOTEBOOK_NAME = "learn_bioinfo.ipynb"
OUTPUT_DIR = Path("extracted_code_cells")

# 2. Create an output folder so your directory doesn't get cluttered
OUTPUT_DIR.mkdir(exist_ok=True)

# 3. Read and parse the notebook JSON structure
notebook_path = Path(NOTEBOOK_NAME)

if not notebook_path.exists():
    print(f"Error: Could not find '{NOTEBOOK_NAME}' in this directory.")
else:
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook_data = json.load(f)

    # 4. Loop through the cells and export each code cell
    cell_counter = 1
    for cell in notebook_data.get("cells", []):
        if cell.get("cell_type") == "code":
            # Combine the lines of code within the cell
            code_content = "".join(cell.get("source", []))
            
            # Skip completely empty cells
            if not code_content.strip():
                continue
                
            # Create a sequential filename (e.g., cell_01.py, cell_02.py)
            filename = OUTPUT_DIR / f"cell_{cell_counter:02d}.py"
            
            # Write the code to the individual file
            filename.write_text(code_content, encoding="utf-8")
            print(f"Generated: {filename}")
            
            cell_counter += 1

    print(f"\nSuccess! Extracted {cell_counter - 1} code cells into the '{OUTPUT_DIR}' folder.")