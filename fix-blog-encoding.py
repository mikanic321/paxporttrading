#!/usr/bin/env python3
"""
Fix blog HTML files encoding issues
- Fix garbled characters (�? etc.)
- Ensure UTF-8 encoding
- Standardize styles with main page
"""

import os
import re

# Blog files to fix
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

# Character replacements for common garbled sequences
replacements = {
    '�?': '→',  # Arrow
    '�': '•',   # Bullet point
    '�?': '✓',  # Checkmark
    '�?': '✅',  # Checkmark emoji
    '�?': '⚠️',  # Warning emoji
    '�?': '💡',  # Lightbulb
    '�?': '🏆',  # Trophy
    '�?': '📦',  # Package
    '�?': '🆕',  # New
    '�?': '🏭',  # Factory
    '�?': '🌱',  # Plant/seedling
    '�?': '🧵',  # Thread
    '�?': '🎨',  # Art palette
    '�?': '⚡',  # Lightning
    '�?': '🔍',  # Magnifying glass
    '�?': '📋',  # Clipboard
    '�?': '📊',  # Chart
    '�?': '✅',  # Checkmark
    '�?': '❌',  # X mark
    '�?': '👍',  # Thumbs up
    '�?': '👎',  # Thumbs down
    '�?': '📅',  # Calendar
    '�?': '⏱️',  # Timer
    '�?': '👤',  # Person
    '�?': '🌍',  # Globe
    '�?': '🏠',  # Home
    '�?': '🏢',  # Office
    '�?': '🚢',  # Ship
    '�?': '✈️',  # Plane
    '�?': '📦',  # Package
    '�?': '💰',  # Money
    '�?': '💵',  # Dollar
    '�?': '📈',  # Chart up
    '�?': '📉',  # Chart down
    '�?': '⭐',  # Star
    '�?': '🔥',  # Fire
    '�?': '🎯',  # Target
    '�?': '🚀',  # Rocket
    '�?': '🔧',  # Wrench
    '�?': '🔨',  # Hammer
    '�?': '📐',  # Triangular ruler
    '�?': '📏',  # Ruler
    '�?': '✂️',  # Scissors
    '�?': '📎',  # Paperclip
    '�?': '📌',  # Pushpin
    '�?': '📍',  # Location pin
    '�?': '🔒',  # Lock
    '�?': '🔓',  # Unlock
    '�?': '🔑',  # Key
    '�?': '🏷️',  # Label
    '�?': '🏷',   # Label
    '�?': '📜',  # Scroll
    '�?': '📃',  # Page
    '�?': '📄',  # Document
    '�?': '📑',  # Bookmark
    '�?': '📚',  # Books
    '�?': '📖',  # Open book
    '�?': '📕',  # Book
    '�?': '📗',  # Green book
    '�?': '📘',  # Blue book
    '�?': '📙',  # Orange book
    '�?': '📓',  # Notebook
    '�?': '📔',  # Notebook with decorative cover
    '�?': '📒',  # Ledger
    '�?': '📰',  # Newspaper
    '�?': '🗞️',  # Rolled newspaper
    '�?': '🗞',   # Rolled newspaper
    '�?': '📺',  # TV
    '�?': '📻',  # Radio
    '�?': '📡',  # Satellite
    '�?': '🔊',  # Speaker
    '�?': '🔉',  # Speaker medium
    '�?': '🔈',  # Speaker low
    '�?': '🔇',  # Mute
    '�?': '📢',  # Loudspeaker
    '�?': '📣',  # Megaphone
    '�?': '📯',  # Postal horn
    '�?': '🔔',  # Bell
    '�?': '🔕',  # Bell with slash
    '�?': '🎵',  # Musical note
    '�?': '🎶',  # Musical notes
    '�?': '🎼',  # Musical score
    '�?': '🎤',  # Microphone
    '�?': '🎧',  # Headphone
    '�?': '🎷',  # Saxophone
    '�?': '🎸',  # Guitar
    '�?': '🎹',  # Piano
    '�?': '🎺',  # Trumpet
    '�?': '🎻',  # Violin
    '�?': '🥁',  # Drum
    '�?': '🎬',  # Clapper board
    '�?': '🏹',  # Bow and arrow
}

def fix_file_encoding(filepath):
    """Fix encoding issues in a single file"""
    try:
        # Read file with UTF-8 encoding
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Track changes
        changes = 0
        
        # Replace garbled characters
        for garbled, correct in replacements.items():
            if garbled in content:
                count = content.count(garbled)
                content = content.replace(garbled, correct)
                changes += count
        
        # Fix common patterns
        # Fix any remaining �? patterns
        content = re.sub(r'�\?', '•', content)
        content = re.sub(r'�', '', content)  # Remove standalone replacement chars
        
        # Write back with UTF-8 encoding and BOM for Windows compatibility
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return changes
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return -1

def main():
    base_dir = "C:/Users/bear/Documents/GitHub/paxporttrading"
    
    total_changes = 0
    files_processed = 0
    
    for filepath in blog_files:
        full_path = os.path.join(base_dir, filepath)
        if os.path.exists(full_path):
            changes = fix_file_encoding(full_path)
            if changes >= 0:
                files_processed += 1
                total_changes += changes
                print(f"✓ {filepath}: {changes} replacements")
            else:
                print(f"✗ {filepath}: ERROR")
        else:
            print(f"✗ {filepath}: NOT FOUND")
    
    print(f"\n{'='*60}")
    print(f"Processed: {files_processed} files")
    print(f"Total replacements: {total_changes}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
