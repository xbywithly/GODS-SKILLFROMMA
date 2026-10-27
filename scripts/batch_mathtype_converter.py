# -*- coding: utf-8 -*-
"""
Thesis MathType Batch Converter
Automatically searches for '$...$' in a Word document and converts each to a MathType OLE object (Equation.DSMT4).
Must be run in an interactive Windows session (Session 1) or via schtasks /it.
"""

import os
import sys
import time
import win32com.client as win32

def convert_document(doc_path):
    if not os.path.isabs(doc_path):
        doc_path = os.path.abspath(doc_path)
    
    print(f"=== MathType Batch Conversion Start ===")
    print(f"Target document: {doc_path}")
    
    if not os.path.exists(doc_path):
        print(f"Error: Document does not exist: {doc_path}")
        sys.exit(1)

    word = win32.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0

    try:
        doc = word.Documents.Open(doc_path)
        print(f"Document opened successfully. Paragraphs: {doc.Paragraphs.Count}")

        converted_count = 0
        start_time = time.time()

        while True:
            rng = doc.Content
            find = rng.Find
            find.ClearFormatting()
            find.Text = "$*$"
            find.MatchWildcards = True
            find.Forward = True
            find.Wrap = 0  # wdFindStop

            if not find.Execute():
                break

            found_text = rng.Text
            found_start = rng.Start
            t0 = time.time()

            rng.Select()
            try:
                word.Application.Run("MTCommand_TeXToggle")
                converted_count += 1
                dt = time.time() - t0
                if converted_count % 5 == 0 or converted_count == 1:
                    print(f"Converted #{converted_count} at pos {found_start} in {dt:.2f}s (TeX snippet: {found_text[:25]}...)")
            except Exception as e:
                print(f"Error converting at pos {found_start} text '{found_text}': {e}")
                # Move forward to avoid infinite loop
                rng.Start = rng.End + 1

        total_time = time.time() - start_time
        print(f"Total equations converted: {converted_count} in {total_time:.2f}s")

        doc.Save()
        doc.Close()
        print("Word document saved and closed.")

    finally:
        word.Quit()
        print("Word application quit.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python batch_mathtype_converter.py <path_to_docx>")
        sys.exit(1)
    convert_document(sys.argv[1])
