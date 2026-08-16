#!/usr/bin/env python3
"""
Resume Build Pipeline Engine
============================
Author: Muhamad Hendri Febriansyah & AI Assistant
Usage:
    python scripts/build_resume.py                 # Builds default (general)
    python scripts/build_resume.py --target all    # Builds all variants (general, frontend, android, web3)
    python scripts/build_resume.py --target frontend
    python scripts/build_resume.py --target android
    python scripts/build_resume.py --target web3
"""

import os
import sys
import json
import argparse
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn

# Fix Windows console UTF-8 output
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Root workspace directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(BASE_DIR, 'data')
TEMPLATES_DIR = os.path.join(DATA_DIR, 'templates')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
VARIANTS_DIR = os.path.join(OUTPUT_DIR, 'variants')


def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def set_cell_margins(cell, top=20, bottom=20, left=0, right=0):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def build_docx(profile, skills, template, output_docx_path):
    doc = docx.Document()
    
    # Page setup - Margins 0.55 inch
    section = doc.sections[0]
    section.top_margin = Inches(0.55)
    section.bottom_margin = Inches(0.55)
    section.left_margin = Inches(0.6)
    section.right_margin = Inches(0.6)
    section.page_width = Inches(8.5)
    section.page_height = Inches(11.0)
    
    PRIMARY_COLOR = RGBColor(24, 33, 47)      # Dark Slate #18212F
    TEXT_COLOR = RGBColor(33, 37, 41)         # Off-black #212529
    MUTED_COLOR = RGBColor(71, 85, 105)       # Slate #475569
    
    # Base typography
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(10.5)
    font.color.rgb = TEXT_COLOR
    
    def add_heading(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title.upper())
        run.bold = True
        run.font.size = Pt(11.5)
        run.font.color.rgb = PRIMARY_COLOR
        
        pPr = p._element.get_or_add_pPr()
        border_xml = parse_xml(
            '<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            '<w:bottom w:val="single" w:sz="6" w:space="2" w:color="18212F"/>'
            '</w:pBdr>'
        )
        pPr.append(border_xml)

    # 1. Header (Name & Contact)
    p_name = doc.add_paragraph()
    p_name.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_name.paragraph_format.space_before = Pt(0)
    p_name.paragraph_format.space_after = Pt(2)
    r_name = p_name.add_run(profile['name'])
    r_name.bold = True
    r_name.font.size = Pt(16)
    r_name.font.color.rgb = PRIMARY_COLOR
    
    c = profile['contact']
    contact_line = f"{c['location']}  |  {c['email']}  |  {c['phone']}  |  {c['linkedin']}  |  {c['portfolio']}"
    p_contact = doc.add_paragraph()
    p_contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_contact.paragraph_format.space_before = Pt(0)
    p_contact.paragraph_format.space_after = Pt(6)
    r_contact = p_contact.add_run(contact_line)
    r_contact.font.size = Pt(9.5)
    r_contact.font.color.rgb = MUTED_COLOR

    # 2. Professional Summary
    add_heading('Summary')
    summary_text = profile['summaries'].get(template['summary_key'], profile['summaries']['general'])
    p_sum = doc.add_paragraph()
    p_sum.paragraph_format.space_before = Pt(2)
    p_sum.paragraph_format.space_after = Pt(4)
    p_sum.paragraph_format.line_spacing = 1.15
    r_sum = p_sum.add_run(summary_text)
    r_sum.font.size = Pt(10)

    # Helper for job headers
    def add_table_header(col1_text, col2_text):
        table = doc.add_table(rows=1, cols=2)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        table.columns[0].width = Inches(5.4)
        table.columns[1].width = Inches(1.9)
        
        c0, c1 = table.cell(0, 0), table.cell(0, 1)
        set_cell_margins(c0, top=20, bottom=5, left=0, right=0)
        set_cell_margins(c1, top=20, bottom=5, left=0, right=0)
        
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(3)
        p0.paragraph_format.space_after = Pt(1)
        r0 = p0.add_run(col1_text)
        r0.bold = True
        r0.font.size = Pt(10.5)
        r0.font.color.rgb = PRIMARY_COLOR
        
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p1.paragraph_format.space_before = Pt(3)
        p1.paragraph_format.space_after = Pt(1)
        r1 = p1.add_run(col2_text)
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = MUTED_COLOR

    def add_bullet(text, is_first=False, is_last=False):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(1 if not is_first else 2)
        p.paragraph_format.space_after = Pt(3 if is_last else 1)
        p.paragraph_format.line_spacing = 1.12
        r = p.add_run(text)
        r.font.size = Pt(10)

    # 3. Work Experience
    add_heading('Experience')
    exp_map = {exp['id']: exp for exp in profile['experiences']}
    ordered_ids = template.get('experience_order', [exp['id'] for exp in profile['experiences']])
    
    for eid in ordered_ids:
        if eid in exp_map:
            exp = exp_map[eid]
            role_header = f"{exp['role']} | {exp['company']}"
            add_table_header(role_header, exp['period'])
            for idx, bullet in enumerate(exp['bullets']):
                add_bullet(bullet, is_first=(idx == 0), is_last=(idx == len(exp['bullets']) - 1))

    # 4. Technical Skills
    add_heading('Skills')
    target_skills = skills.get(template['skills_key'], skills['general'])
    for cat in target_skills:
        p_skill = doc.add_paragraph()
        p_skill.paragraph_format.space_before = Pt(1)
        p_skill.paragraph_format.space_after = Pt(2)
        p_skill.paragraph_format.line_spacing = 1.1
        r_cat = p_skill.add_run(f"{cat['category']}: ")
        r_cat.bold = True
        r_cat.font.size = Pt(10)
        r_items = p_skill.add_run(cat['items'])
        r_items.font.size = Pt(10)

    # 5. Education
    add_heading('Education')
    for edu in profile['education']:
        add_table_header(f"{edu['institution']} | {edu['degree'].split('in')[0].strip()}", edu['period'])
        p_edu = doc.add_paragraph()
        p_edu.paragraph_format.space_before = Pt(0)
        p_edu.paragraph_format.space_after = Pt(4)
        r_edu = p_edu.add_run(f"Bachelor of Computer Science (S.Kom.) | GPA: {edu['gpa']} | Focus: {edu['focus']}")
        r_edu.font.size = Pt(9.5)
        r_edu.font.color.rgb = MUTED_COLOR

    # 6. Certifications
    add_heading('Certifications')
    for cert in profile['certifications']:
        add_table_header(f"{cert['title']} | {cert['issuer']}", cert['period'])
        if 'focus' in cert:
            p_cert_det = doc.add_paragraph()
            p_cert_det.paragraph_format.space_before = Pt(0)
            p_cert_det.paragraph_format.space_after = Pt(3)
            p_cert_det.paragraph_format.left_indent = Inches(0.2)
            r_det = p_cert_det.add_run(f"Focus: {cert['focus']}")
            r_det.font.size = Pt(9.5)
            r_det.font.color.rgb = MUTED_COLOR

    # 7. Languages
    add_heading('Languages')
    p_lang = doc.add_paragraph()
    p_lang.paragraph_format.space_before = Pt(2)
    p_lang.paragraph_format.space_after = Pt(4)
    lang_parts = []
    for lang in profile['languages']:
        r_l = p_lang.add_run(f"{lang['language']}: ")
        r_l.bold = True
        r_l.font.size = Pt(10)
        p_lang.add_run(f"{lang['proficiency']}    ")

    os.makedirs(os.path.dirname(output_docx_path), exist_ok=True)
    doc.save(output_docx_path)
    print(f"  [DOCX] -> {output_docx_path}")


def build_markdown(profile, skills, template, output_md_path):
    c = profile['contact']
    summary_text = profile['summaries'].get(template['summary_key'], profile['summaries']['general'])
    target_skills = skills.get(template['skills_key'], skills['general'])
    exp_map = {exp['id']: exp for exp in profile['experiences']}
    ordered_ids = template.get('experience_order', [exp['id'] for exp in profile['experiences']])

    lines = []
    lines.append(f"# {profile['name']}")
    lines.append(f"{c['location']} | {c['email']} | {c['phone']}")
    lines.append(f"[LinkedIn: {c['linkedin']}]({c['linkedin_url']}) | [Portfolio: {c['portfolio']}]({c['portfolio_url']}) | [GitHub: {c['github']}]({c['github_url']})\n")
    lines.append("---\n")
    lines.append("## PROFESSIONAL SUMMARY")
    lines.append(summary_text + "\n")
    lines.append("---\n")
    lines.append("## WORK EXPERIENCE\n")

    for eid in ordered_ids:
        if eid in exp_map:
            exp = exp_map[eid]
            lines.append(f"### {exp['role']} | {exp['company']}")
            lines.append(f"*{exp['period']}*\n")
            for b in exp['bullets']:
                lines.append(f"- {b}")
            lines.append("")

    lines.append("---\n")
    lines.append("## TECHNICAL SKILLS\n")
    for cat in target_skills:
        lines.append(f"- **{cat['category']}:** {cat['items']}")
    lines.append("")

    lines.append("---\n")
    lines.append("## EDUCATION\n")
    for edu in profile['education']:
        lines.append(f"### {edu['institution']}")
        lines.append(f"**{edu['degree']}** | *{edu['period']}*")
        lines.append(f"- **GPA:** {edu['gpa']}")
        lines.append(f"- **Focus Area:** {edu['focus']}\n")

    lines.append("---\n")
    lines.append("## CERTIFICATIONS\n")
    for cert in profile['certifications']:
        lines.append(f"- **{cert['title']}** – {cert['issuer']} *({cert['period']})*")
        if 'focus' in cert:
            lines.append(f"  *Focus: {cert['focus']}*")
    lines.append("")

    lines.append("---\n")
    lines.append("## LANGUAGES")
    for lang in profile['languages']:
        lines.append(f"- **{lang['language']}:** {lang['proficiency']}")

    content = "\n".join(lines) + "\n"
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  [MD]   -> {output_md_path}")


def convert_to_pdf(docx_path, pdf_path):
    try:
        import win32com.client
        word = win32com.client.Dispatch('Word.Application')
        word.Visible = False
        try:
            wdoc = word.Documents.Open(os.path.abspath(docx_path))
            wdoc.SaveAs(os.path.abspath(pdf_path), FileFormat=17)
            wdoc.Close()
            print(f"  [PDF]  -> {pdf_path}")
        finally:
            word.Quit()
    except Exception as e:
        print(f"  [PDF Warning] Could not convert via Word COM: {e}")


def process_target(target_name, profile, skills):
    template_path = os.path.join(TEMPLATES_DIR, f"{target_name}.json")
    if not os.path.exists(template_path):
        print(f"Error: Template {template_path} not found.")
        return

    template = load_json(template_path)
    base_name = template.get('output_filename', f"Resume_{target_name.capitalize()}")
    
    # Paths
    if target_name == 'general':
        docx_path = os.path.join(OUTPUT_DIR, f"{base_name}.docx")
        pdf_path = os.path.join(OUTPUT_DIR, f"{base_name}.pdf")
        md_path = os.path.join(OUTPUT_DIR, f"{base_name}.md")
        
        # Also mirror to root workspace for immediate convenience
        root_docx = os.path.join(BASE_DIR, "Muhamad Hendri Febriansyah - Resume.docx")
        root_pdf = os.path.join(BASE_DIR, "Muhamad Hendri Febriansyah - Resume.pdf")
    else:
        docx_path = os.path.join(VARIANTS_DIR, f"{base_name}.docx")
        pdf_path = os.path.join(VARIANTS_DIR, f"{base_name}.pdf")
        md_path = os.path.join(VARIANTS_DIR, f"{base_name}.md")

    print(f"\n🚀 Generating [{template.get('display_title', target_name)}]...")
    build_docx(profile, skills, template, docx_path)
    build_markdown(profile, skills, template, md_path)
    convert_to_pdf(docx_path, pdf_path)
    
    if target_name == 'general':
        import shutil
        shutil.copy2(docx_path, root_docx)
        shutil.copy2(pdf_path, root_pdf)


def main():
    parser = argparse.ArgumentParser(description="Resume Build Pipeline")
    parser.add_argument('--target', default='general', help="Target template: general, frontend, android, web3, all")
    args = parser.parse_args()

    profile_path = os.path.join(DATA_DIR, 'profile.json')
    skills_path = os.path.join(DATA_DIR, 'skills.json')

    if not os.path.exists(profile_path) or not os.path.exists(skills_path):
        print("Error: profile.json or skills.json not found in data/ folder.")
        sys.exit(1)

    profile = load_json(profile_path)
    skills = load_json(skills_path)

    if args.target == 'all':
        targets = ['general', 'frontend', 'android', 'web3']
        for t in targets:
            process_target(t, profile, skills)
    else:
        process_target(args.target, profile, skills)

    print("\n✅ All target builds completed successfully!")


if __name__ == '__main__':
    main()
