import fitz  # PyMuPDF
import os
import json

# Paths
pdf_files = [
    r"C:\Users\rattu\Downloads\PORTER_NN\Doc File\porter-neural-networks-regression.pdf",
    r"C:\Users\rattu\Downloads\PORTER_NN\Doc File\Ratnesh_Porter_Case_Study.pdf"
]
output_dir = r"C:\Users\rattu\Downloads\PORTER_NN\frontend\public\graphs"

# Create output directory
os.makedirs(output_dir, exist_ok=True)

graph_data = []
image_count = 0

for pdf_path in pdf_files:
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        continue
        
    print(f"Processing {pdf_path}...")
    try:
        doc = fitz.open(pdf_path)
        for i in range(len(doc)):
            page = doc[i]
            
            # Get text for context
            page_text = page.get_text("text").strip()
            caption = page_text[:200].replace('\n', ' ') + "..." if len(page_text) > 200 else page_text
            
            # Render the ENTIRE page to ensure we capture all graph elements (axes, legends, titles)
            # Zoom = 2 for better resolution
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            
            image_filename = f"page_{image_count}.png"
            image_path = os.path.join(output_dir, image_filename)
            
            pix.save(image_path)
            
            graph_data.append({
                "id": image_count,
                "src": f"graphs/{image_filename}",
                "context": caption,
                "source_pdf": os.path.basename(pdf_path),
                "page": i + 1
            })
            
            print(f"Saved Page {i+1} as {image_filename}")
            image_count += 1
                    
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")

# Save manifest
manifest_path = r"C:\Users\rattu\Downloads\PORTER_NN\frontend\src\graphs.json"
with open(manifest_path, "w") as f:
    json.dump(graph_data, f, indent=2)

print(f"Extraction complete. {image_count} graphs processed.")
print(f"Manifest saved to {manifest_path}")
