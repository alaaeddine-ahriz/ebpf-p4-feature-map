#!/usr/bin/env python3
"""
P4 Test Results Analyzer

Analyzes CSV files containing P4 compilation test results and generates statistics
showing pass/fail percentages for different sections (control, parser, top-level)
and categories (statements, declarations, expressions).
"""

import csv
import os
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, TextIO
from datetime import datetime


def parse_filename(filename: str) -> Tuple[str, str]:
    """
    Parse filename to extract section and category.
    
    Args:
        filename: CSV filename (e.g., 'results_control_statements.csv')
    
    Returns:
        Tuple of (section, category) or (None, None) if not a valid results file
    """
    if not filename.startswith('results_') or not filename.endswith('.csv'):
        return None, None
    
    # Remove 'results_' prefix and '.csv' suffix
    name = filename[8:-4]
    
    # Handle expressions (no section prefix)
    if name == 'expressions':
        return 'general', 'expressions'
    
    # Split by underscore to get section and category
    parts = name.split('_', 1)
    if len(parts) == 2:
        section = parts[0]  # e.g., 'control', 'parser', 'top-level'
        category = parts[1]  # e.g., 'statements', 'declarations'
        return section, category
    
    return None, None


def analyze_csv(filepath: Path) -> Dict[str, Dict[str, int]]:
    """
    Analyze a single CSV file and count PASS/FAIL for P4Cherry and P4C-eBPF.
    
    Args:
        filepath: Path to the CSV file
    
    Returns:
        Dictionary with counts for each compiler:
        {
            'P4Cherry': {'pass': X, 'fail': Y, 'total': Z},
            'P4C-eBPF': {'pass': X, 'fail': Y, 'total': Z}
        }
    """
    results = {
        'P4Cherry': {'pass': 0, 'fail': 0, 'total': 0},
        'P4C-eBPF': {'pass': 0, 'fail': 0, 'total': 0}
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                # Skip empty rows
                if not row.get('Grammar'):
                    continue
                
                # Count P4Cherry results
                p4cherry_result = row.get('P4Cherry', '').strip().upper()
                if p4cherry_result == 'PASS':
                    results['P4Cherry']['pass'] += 1
                    results['P4Cherry']['total'] += 1
                elif p4cherry_result == 'FAIL':
                    results['P4Cherry']['fail'] += 1
                    results['P4Cherry']['total'] += 1
                
                # Count P4C-eBPF results
                p4c_result = row.get('P4C-eBPF', '').strip().upper()
                if p4c_result == 'PASS':
                    results['P4C-eBPF']['pass'] += 1
                    results['P4C-eBPF']['total'] += 1
                elif p4c_result == 'FAIL':
                    results['P4C-eBPF']['fail'] += 1
                    results['P4C-eBPF']['total'] += 1
    
    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)
    
    return results


def calculate_percentage(passed: int, total: int) -> float:
    """Calculate pass percentage."""
    if total == 0:
        return 0.0
    return (passed / total) * 100


def print_statistics(stats: Dict[str, Dict[str, Dict[str, Dict[str, int]]]], file: TextIO = None):
    """
    Print formatted statistics.
    
    Args:
        stats: Nested dictionary structure:
               {section: {category: {compiler: {pass, fail, total}}}}
        file: Optional file object to write to (defaults to stdout)
    """
    print("\n" + "="*80, file=file)
    print("P4 COMPILATION TEST RESULTS ANALYSIS", file=file)
    print("="*80 + "\n", file=file)
    
    # Sort sections for consistent output
    sections = sorted(stats.keys())
    
    for section in sections:
        print(f"\n{'─'*80}", file=file)
        print(f"SECTION: {section.upper()}", file=file)
        print(f"{'─'*80}", file=file)
        
        categories = sorted(stats[section].keys())
        
        for category in categories:
            print(f"\n  Category: {category.title()}", file=file)
            print(f"  {'-'*76}", file=file)
            
            compilers = ['P4Cherry', 'P4C-eBPF']
            
            for compiler in compilers:
                data = stats[section][category][compiler]
                pass_count = data['pass']
                fail_count = data['fail']
                total_count = data['total']
                pass_pct = calculate_percentage(pass_count, total_count)
                fail_pct = calculate_percentage(fail_count, total_count)
                
                print(f"\n    {compiler}:", file=file)
                print(f"      Total Tests:  {total_count}", file=file)
                print(f"      Passed:       {pass_count:3d}  ({pass_pct:6.2f}%)", file=file)
                print(f"      Failed:       {fail_count:3d}  ({fail_pct:6.2f}%)", file=file)
    
    print("\n" + "="*80 + "\n", file=file)


def print_summary(stats: Dict[str, Dict[str, Dict[str, Dict[str, int]]]], file: TextIO = None):
    """
    Print summary statistics across all sections.
    
    Args:
        stats: Nested dictionary structure
        file: Optional file object to write to (defaults to stdout)
    """
    print("\n" + "="*80, file=file)
    print("OVERALL SUMMARY", file=file)
    print("="*80 + "\n", file=file)
    
    # Aggregate totals
    overall = {
        'P4Cherry': {'pass': 0, 'fail': 0, 'total': 0},
        'P4C-eBPF': {'pass': 0, 'fail': 0, 'total': 0}
    }
    
    for section in stats.values():
        for category in section.values():
            for compiler in ['P4Cherry', 'P4C-eBPF']:
                overall[compiler]['pass'] += category[compiler]['pass']
                overall[compiler]['fail'] += category[compiler]['fail']
                overall[compiler]['total'] += category[compiler]['total']
    
    for compiler in ['P4Cherry', 'P4C-eBPF']:
        data = overall[compiler]
        pass_pct = calculate_percentage(data['pass'], data['total'])
        fail_pct = calculate_percentage(data['fail'], data['total'])
        
        print(f"{compiler}:", file=file)
        print(f"  Total Tests:  {data['total']}", file=file)
        print(f"  Passed:       {data['pass']:3d}  ({pass_pct:6.2f}%)", file=file)
        print(f"  Failed:       {data['fail']:3d}  ({fail_pct:6.2f}%)", file=file)
        print(file=file)
    
    print("="*80 + "\n", file=file)


def main():
    """Main function to analyze P4 test results."""
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Usage: python analyze_results.py <directory> [output_file]")
        print("\nArguments:")
        print("  directory    : Directory containing results_*.csv files")
        print("  output_file  : Optional output file name (default: analysis_results_TIMESTAMP.txt)")
        print("\nExamples:")
        print("  python analyze_results.py .")
        print("  python analyze_results.py /path/to/results")
        print("  python analyze_results.py . my_analysis.txt")
        sys.exit(1)
    
    # Get directory from command line
    directory = Path(sys.argv[1])
    
    # Get output file (optional, use default if not provided)
    if len(sys.argv) >= 3:
        output_file = Path(sys.argv[2])
    else:
        # Generate default filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = Path(f"analysis_results_{timestamp}.txt")
    
    if not directory.exists():
        print(f"Error: Directory '{directory}' does not exist.", file=sys.stderr)
        sys.exit(1)
    
    if not directory.is_dir():
        print(f"Error: '{directory}' is not a directory.", file=sys.stderr)
        sys.exit(1)
    
    # Find all CSV files
    csv_files = list(directory.glob('results_*.csv'))
    
    if not csv_files:
        print(f"No results CSV files found in '{directory}'.", file=sys.stderr)
        print("Looking for files matching pattern: results_*.csv", file=sys.stderr)
        sys.exit(1)
    
    print(f"Found {len(csv_files)} CSV file(s) in '{directory}'")
    
    # Structure: {section: {category: {compiler: {pass, fail, total}}}}
    stats = defaultdict(lambda: defaultdict(lambda: {
        'P4Cherry': {'pass': 0, 'fail': 0, 'total': 0},
        'P4C-eBPF': {'pass': 0, 'fail': 0, 'total': 0}
    }))
    
    # Analyze each CSV file
    for csv_file in sorted(csv_files):
        section, category = parse_filename(csv_file.name)
        
        if section is None or category is None:
            print(f"Skipping '{csv_file.name}' (invalid format)", file=sys.stderr)
            continue
        
        print(f"  - Analyzing: {csv_file.name} [{section} / {category}]")
        
        results = analyze_csv(csv_file)
        
        # Store results in stats structure
        stats[section][category] = results
    
    # Print statistics to console
    print_statistics(stats)
    print_summary(stats)
    
    # Write statistics to file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            # Write header with metadata
            print(f"P4 Compilation Test Results Analysis", file=f)
            print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", file=f)
            print(f"Source Directory: {directory.absolute()}", file=f)
            print(f"Total CSV Files Analyzed: {len(csv_files)}", file=f)
            
            # Write statistics
            print_statistics(stats, file=f)
            print_summary(stats, file=f)
        
        print(f"\n✓ Results saved to: {output_file.absolute()}")
        
    except Exception as e:
        print(f"\nError writing to file '{output_file}': {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

