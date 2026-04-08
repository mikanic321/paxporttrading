#!/usr/bin/env python3
"""Verify and report encoding issues in blog HTML files"""

import os
import re

blog_files = [
    "blog/how-to-verify-chinese-suppliers-guide.html",
    "blog/import-from-china-to-kenya-complete-guide.html",
    "blog/10-common-mistakes-importing-china.html",
    "blog/how-to-negotiate-chinese-suppliers-guide.html",
    "blog/alibaba-vs-1688-sourcing-guide.html",
    "blog/china-import-documents-checklist.html",
    "blog/how-to-calculate-landed-cost-china-imports.html",
    "blog/how-to-choose-shipping-method-china.html",
    "blog/how-to-find-reliable-sourcing-agent-china-2026.html",
    "blog/amazon-fba-sourcing-china-complete-guide.html",
    "blog/quality-control-importing-china-checklist.html",
    "blog/shipping-from-china-fob-cif-ddp-explained.html",
    "blog/textile-sourcing-china-complete-guide.html",
    "blog/nigeria-sourcing-guide.html",
    "blog/africa-construction-materials-sourcing.html"
]

def check_file(filepath):
    """Check file for encoding issues"""
    issues = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Check for replacement character
        if '\ufffd' in content:
            # Find lines with replacement character
            lines = content.split('\n')
            for i, line in enumerate(lines, 1):
                if '\ufffd' in line:
                    issues.append(f"Line {i}: {line.strip()[:100]}")
        
        # Check for other common garbled patterns
        garbled_patterns = [
            '�?',
            '�',
        ]
        for pattern in garbled_patterns:
            if pattern in content:
                lines = content.split('\n')
                for i, line in enumerate(lines, 1):
                    if pattern in line:
                        issues.append(f"Line {i}: {line.strip()[:100]}")
        
        return issues
    except Exception as e:
        return [f"Error reading file: {e}"]

def main():
    base_dir = "C:/Users/bear/Documents/GitHub/paxporttrading"
    
    total_issues = 0
    files_with_issues = 0
    
    print("="*80)
    print("ENCODING VERIFICATION REPORT")
    print("="*80)
    
    for filepath in blog_files:
        full_path = os.path.join(base_dir, filepath)
        if os.path.exists(full_path):
            issues = check_file(full_path)
            if issues:
                files_with_issues += 1
                total_issues += len(issues)
                print(f"\n❌ {filepath}")
                for issue in issues[:5]:  # Show first 5 issues
                    print(f"   {issue}")
                if len(issues) > 5:
                    print(f"   ... and {len(issues) - 5} more issues")
            else:
                print(f"✓ {filepath}")
        else:
            print(f"⚠ {filepath} - NOT FOUND")
    
    print("\n" + "="*80)
    print(f"SUMMARY: {files_with_issues} files with {total_issues} total issues")
    print("="*80)

if __name__ == "__main__":
    main()
