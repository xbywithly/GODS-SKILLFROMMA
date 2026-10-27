# -*- coding: utf-8 -*-
"""
Thesis MathTab Post-Processor
Directly updates docx word/document.xml to guarantee standard MathTab alignment:
- Page margins: Left 2.5 cm, Right 2.5 cm (text width 16.0 cm = 9074 dxa)
- Formula paragraphs: Zero indent, atLeast 22pt (440 dxa) line spacing, 6pt before/after
- Center tab at 4540 dxa (8.01 cm), Right tab at 9080 dxa (16.02 cm)
"""

import os
import sys
import re
import zipfile
import shutil
import xml.etree.ElementTree as ET

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
ET.register_namespace('w', W_NS)

def format_equation_pPr(pPr):
    # 1. Zero indent
    ind = pPr.find(f"{{{W_NS}}}ind")
    if ind is None:
        ind = ET.SubElement(pPr, f"{{{W_NS}}}ind")
    ind.set(f"{{{W_NS}}}firstLine", "0")
    ind.set(f"{{{W_NS}}}firstLineChars", "0")
    ind.set(f"{{{W_NS}}}left", "0")
    ind.set(f"{{{W_NS}}}right", "0")

    # 2. Left paragraph alignment so tabs control positioning
    jc = pPr.find(f"{{{W_NS}}}jc")
    if jc is None:
        jc = ET.SubElement(pPr, f"{{{W_NS}}}jc")
    jc.set(f"{{{W_NS}}}val", "left")

    # 3. Line spacing atLeast 22pt (440 dxa) to prevent formula vertical clipping
    spacing = pPr.find(f"{{{W_NS}}}spacing")
    if spacing is None:
        spacing = ET.SubElement(pPr, f"{{{W_NS}}}spacing")
    spacing.set(f"{{{W_NS}}}line", "440")
    spacing.set(f"{{{W_NS}}}lineRule", "atLeast")
    spacing.set(f"{{{W_NS}}}before", "120")
    spacing.set(f"{{{W_NS}}}after", "120")

    # 4. Standard MathTab tab stops: Center at 4540, Right at 9080
    tabs = pPr.find(f"{{{W_NS}}}tabs")
    if tabs is not None:
        pPr.remove(tabs)
    tabs = ET.SubElement(pPr, f"{{{W_NS}}}tabs")
    
    t_center = ET.SubElement(tabs, f"{{{W_NS}}}tab")
    t_center.set(f"{{{W_NS}}}val", "center")
    t_center.set(f"{{{W_NS}}}pos", "4540")
    
    t_right = ET.SubElement(tabs, f"{{{W_NS}}}tab")
    t_right.set(f"{{{W_NS}}}val", "right")
    t_right.set(f"{{{W_NS}}}pos", "9080")

def postprocess_mathtab(doc_path):
    if not os.path.exists(doc_path):
        print(f"Error: Document does not exist: {doc_path}")
        sys.exit(1)

    print(f"Post-processing MathTab layout for: {doc_path}")
    temp_dir = doc_path + "_mathtab_temp"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    with zipfile.ZipFile(doc_path, 'r') as zf:
        zf.extractall(temp_dir)

    doc_xml_path = os.path.join(temp_dir, "word", "document.xml")
    tree = ET.parse(doc_xml_path)
    root = tree.getroot()

    body = root.find(f"{{{W_NS}}}body")
    eq_count = 0

    # Ensure page margins: 2.5cm left/right = 1418 dxa, 3.0cm top = 1701 dxa, 2.5cm bottom = 1418 dxa
    sectPr = body.find(f"{{{W_NS}}}sectPr")
    if sectPr is not None:
        pgMar = sectPr.find(f"{{{W_NS}}}pgMar")
        if pgMar is not None:
            pgMar.set(f"{{{W_NS}}}left", "1418")
            pgMar.set(f"{{{W_NS}}}right", "1418")
            pgMar.set(f"{{{W_NS}}}top", "1701")
            pgMar.set(f"{{{W_NS}}}bottom", "1418")

    # Match equation paragraphs: has '(章节号-公式号)' e.g. (2-1), (3-4)
    eq_pattern = re.compile(r'\(\s*\d+\s*[-–]\s*\d+\s*\)')

    for p in body.findall(f"{{{W_NS}}}p"):
        p_text = "".join(p.itertext()).strip()
        if eq_pattern.search(p_text):
            pPr = p.find(f"{{{W_NS}}}pPr")
            if pPr is None:
                pPr = ET.Element(f"{{{W_NS}}}pPr")
                p.insert(0, pPr)
            format_equation_pPr(pPr)
            eq_count += 1

    tree.write(doc_xml_path, xml_declaration=True, encoding="utf-8")

    # Repack zip into docx
    backup_path = doc_path + ".bak"
    shutil.copy2(doc_path, backup_path)
    
    with zipfile.ZipFile(doc_path, 'w', zipfile.ZIP_DEFLATED) as zf_out:
        for root_dir, dirs, files in os.walk(temp_dir):
            for file in files:
                full_f = os.path.join(root_dir, file)
                rel_f = os.path.relpath(full_f, temp_dir)
                zf_out.write(full_f, rel_f)

    shutil.rmtree(temp_dir)
    if os.path.exists(backup_path):
        os.remove(backup_path)

    print(f"Successfully formatted {eq_count} display equation paragraphs with standard MathTab layout.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python postprocess_mathtab.py <path_to_docx>")
        sys.exit(1)
    postprocess_mathtab(sys.argv[1])
