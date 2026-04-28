#!/usr/bin/env python3
"""
Spec Scorer - Avalia a qualidade de uma spec de feature
Baseado na rubrica em references/evaluation_rubric.md
"""

import argparse
import json
import re
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class DimensionScore:
    name: str
    weight: float
    raw_score: float
    max_raw: float
    issues: list[str] = field(default_factory=list)
    positives: list[str] = field(default_factory=list)

    @property
    def weighted_score(self) -> float:
        return (self.raw_score / self.max_raw) * self.weight * 100

@dataclass
class SpecReport:
    file: str
    total_score: float
    classification: str
    dimensions: list[DimensionScore]
    critical_gaps: list[str]
    suggestions: list[str]
    raw_text: str

def load_spec(path: str) -> str:
    p = Path(path)
    if not p.exists():
        print(f"[X] Arquivo nao encontrado: {path}", file=sys.stderr)
        sys.exit(1)
    return p.read_text(encoding="utf-8")

def has_section(text: str, section_pattern: str) -> bool:
    return bool(re.search(section_pattern, text, re.IGNORECASE | re.MULTILINE))

def section_content(text: str, section_pattern: str) -> str:
    match = re.search(section_pattern, text, re.IGNORECASE | re.MULTILINE)
    if not match: return ""
    start = match.end()
    # Find next section starting with # or ## followed by a number
    next_section = re.search(r'^#{1,2}\s+\d+\.', text[start:], re.MULTILINE)
    end = start + next_section.start() if next_section else len(text)
    return text[start:end].strip()

def count_pattern(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, re.IGNORECASE | re.MULTILINE))

def has_content(text: str, min_words: int = 10) -> bool:
    words = re.findall(r'\b\w+\b', text)
    return len(words) >= min_words

def count_rf_items(text: str) -> int: return count_pattern(text, r'\bRF-\d+\b')
def count_nf_items(text: str) -> int: return count_pattern(text, r'\bNG-\d+\b')
def count_ec_items(text: str) -> int: return count_pattern(text, r'\bEC-\d+\b')

def has_numeric_metric(text: str) -> bool:
    return bool(re.search(r'[<><=|>=]\s*\d+|=\s*\d+\s*%|\d+\s*(ms|min|h|%|dias|days)', text))

def has_vague_terms(text: str) -> list[str]:
    vague = ["rapidamente", "eficiente", "intuitiva", "facil", "rapido", "bom"]
    found = []
    for term in vague:
        if re.search(r'\b' + re.escape(term) + r'\b', text, re.IGNORECASE): found.append(term)
    return found

def score_completude(text: str) -> DimensionScore:
    dim = DimensionScore(name="Completude", weight=0.30, raw_score=0, max_raw=30)
    score = 0
    sections = [
        (r'^#{1,2}\s+1[\.\s]+Resum', "Resumo"),
        (r'^#{1,2}\s+2[\.\s]+Contexto', "Contexto"),
        (r'^#{1,2}\s+3[\.\s]+Goals', "Goals"),
        (r'^#{1,2}\s+4[\.\s]+Non.Goals', "Non-Goals"),
        (r'^#{1,2}\s+5[\.\s]+Usuari', "Usuarios"),
        (r'^#{1,2}\s+6[\.\s]+Requisitos', "Requisitos"),
    ]
    present = 0
    for pattern, name in sections:
        if has_section(text, pattern):
            if has_content(section_content(text, pattern), 5):
                present += 1
                dim.positives.append(f"[OK] {name} preenchida")
            else: dim.issues.append(f"[!] {name} insuficiente")
        else: dim.issues.append(f"[X] {name} ausente")
    score += (present / len(sections)) * 10
    
    rf_count = count_rf_items(text)
    if rf_count >= 3: score += 10; dim.positives.append(f"[OK] {rf_count} RFs")
    else: dim.issues.append("[X] Poucos RFs")
    
    ng_count = count_nf_items(text)
    if ng_count >= 2: score += 10; dim.positives.append(f"[OK] {ng_count} NGs")
    else: dim.issues.append("[X] Poucos NGs")
    
    dim.raw_score = min(score, dim.max_raw)
    return dim

def score_testabilidade(text: str) -> DimensionScore:
    dim = DimensionScore(name="Testabilidade", weight=0.25, raw_score=0, max_raw=25)
    score = 0
    if not has_vague_terms(text): score += 10; dim.positives.append("[OK] Sem termos vagos")
    if has_section(text, r'Fluxo Principal|Happy Path'): score += 10; dim.positives.append("[OK] Happy Path presente")
    if has_numeric_metric(text): score += 5; dim.positives.append("[OK] Metricas numericas")
    dim.raw_score = min(score, dim.max_raw)
    return dim

def score_clareza(text: str) -> DimensionScore:
    dim = DimensionScore(name="Clareza", weight=0.20, raw_score=0, max_raw=20)
    score = 15 # Start with good score
    if count_pattern(text, r'ABERTO:|OQ-\d+') > 0: score += 5; dim.positives.append("[OK] Open Questions")
    dim.raw_score = min(score, dim.max_raw)
    return dim

def score_escopo(text: str) -> DimensionScore:
    dim = DimensionScore(name="Escopo", weight=0.15, raw_score=0, max_raw=15)
    score = 0
    if count_nf_items(text) >= 2: score += 10; dim.positives.append("[OK] Non-Goals especificos")
    if has_section(text, r'Rollout|Lancamento'): score += 5; dim.positives.append("[OK] Plano de Rollout")
    dim.raw_score = min(score, dim.max_raw)
    return dim

def score_edge_cases(text: str) -> DimensionScore:
    dim = DimensionScore(name="Edge Cases", weight=0.10, raw_score=0, max_raw=10)
    ec_count = count_ec_items(text)
    if ec_count >= 2: dim.raw_score = 10; dim.positives.append(f"[OK] {ec_count} Edge Cases")
    else: dim.issues.append("[X] Falta Edge Cases")
    return dim

def classify(score: float) -> str:
    if score >= 85: return "[*] Excelente - Pronta"
    if score >= 70: return "[OK] Boa - Ajustes menores"
    if score >= 50: return "[!] Regular - Revisar"
    return "[X] Insuficiente"

def build_report(spec_path: str) -> SpecReport:
    text = load_spec(spec_path)
    dims = [score_completude(text), score_testabilidade(text), score_clareza(text), score_escopo(text), score_edge_cases(text)]
    total = sum(d.weighted_score for d in dims)
    return SpecReport(
        file=spec_path, total_score=round(total, 1), classification=classify(total),
        dimensions=dims, critical_gaps=[i for d in dims for i in d.issues if "[X]" in i],
        suggestions=[i for d in dims for i in d.issues if "[!]" in i], raw_text=text
    )

def print_report(report: SpecReport):
    print(f"\n{'='*60}\n  SPEC QUALITY REPORT: {report.file}\n{'='*60}")
    print(f"\n  SCORE TOTAL: {report.total_score}/100  --  {report.classification}\n")
    for d in report.dimensions:
        pct = round(d.raw_score / d.max_raw * 100)
        print(f"  {d.name:<20} {pct:>3}% | Contrib: {round(d.weighted_score, 1):>5} pts")
    if report.critical_gaps:
        print("\n  [X] GAPS CRITICOS:")
        for g in report.critical_gaps: print(f"      {g}")
    print(f"\n{'='*60}\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True)
    args = parser.parse_args()
    report = build_report(args.spec)
    print_report(report)
    sys.exit(0 if report.total_score >= 70 else 1)

if __name__ == "__main__":
    main()