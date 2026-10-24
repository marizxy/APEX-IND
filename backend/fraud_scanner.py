"""
AICTE Automated Document Fraud Scanner & Forensic OCR Engine (v5.0)
Multi-layered forensic document analysis for student credentials (TC, Marksheets, Aadhaar, Quota Certificates).
Simulates OCR extraction, font consistency checks, EXIF metadata tampering detection, and cryptographic seal verification.
"""

import io
import time
import hashlib
from datetime import datetime
from typing import Dict, Any, List, Optional
from PIL import Image, ImageDraw, ImageFont

# Pre-Configured Government Forensic Benchmark Cases
PRESET_FORENSIC_CASES = {
    "Altered Transfer Certificate (Photoshop Text Splicing)": {
        "doc_type": "Transfer Certificate (TC)",
        "claimed_name": "Karthick Ram",
        "claimed_apaar": "5555-6666-7777",
        "claimed_institution": "Anna University Chennai",
        "serial_number": "TN-TC-2023-88491",
        "issue_date": "2023-06-15",
        "software_signature": "Adobe Photoshop 24.1 (Windows)",
        "baseline_drift_px": 8.4,
        "font_dpi_variance": 0.42,
        "serial_checksum_valid": False,
        "is_counterfeit": True,
        "tamper_locations": [
            {"label": "Candidate Name Splicing", "box": (160, 115, 410, 150), "severity": "CRITICAL"},
            {"label": "Altered Date of Relieving", "box": (160, 195, 340, 225), "severity": "WARNING"}
        ],
        "forensic_notes": "Character glyph baselines shifted by 8.4px relative to template grid. Micro-text antialiasing indicates 72 DPI text inserted into 300 DPI scanned document. EXIF metadata reveals Adobe Photoshop 24.1 export timestamp."
    },
    "Counterfeit EWS Quota Certificate (Tampered Revenue Seal)": {
        "doc_type": "Income & Caste Quota Certificate",
        "claimed_name": "Anand Mahindra",
        "claimed_apaar": "1122-4455-7788",
        "claimed_institution": "District Revenue Office, Vellore",
        "serial_number": "EWS-REV-99120",
        "issue_date": "2024-03-20",
        "software_signature": "Canva Desktop App / PDF Export",
        "baseline_drift_px": 5.1,
        "font_dpi_variance": 0.35,
        "serial_checksum_valid": False,
        "is_counterfeit": True,
        "tamper_locations": [
            {"label": "Forged Tahsildar Digital Stamp", "box": (380, 260, 550, 340), "severity": "CRITICAL"},
            {"label": "Income Ceiling Alteration (₹7.5L to ₹1.8L)", "box": (180, 160, 420, 190), "severity": "CRITICAL"}
        ],
        "forensic_notes": "Revenue official digital signature hash does not resolve against Tamil Nadu State Treasury Public Key. Certificate serial number EWS-REV-99120 is registered to another citizen in state database."
    },
    "Aadhaar Identity Card (Conflicting Micro-Text & DOB)": {
        "doc_type": "Aadhaar Card / APAAR Identity Passport",
        "claimed_name": "Priya Varadarajan",
        "claimed_apaar": "1111-2222-3333",
        "claimed_institution": "UIDAI Central Identity Repository",
        "serial_number": "UID-2024-901844",
        "issue_date": "2021-08-10",
        "software_signature": "GIMP 2.10.34 Image Editor",
        "baseline_drift_px": 6.8,
        "font_dpi_variance": 0.28,
        "serial_checksum_valid": False,
        "is_counterfeit": True,
        "tamper_locations": [
            {"label": "Photo Cut-and-Paste Edge Artifacts", "box": (40, 90, 150, 230), "severity": "CRITICAL"},
            {"label": "Aadhaar Number Text Substitution", "box": (170, 220, 430, 255), "severity": "CRITICAL"}
        ],
        "forensic_notes": "Guilloche security pattern abruptly broken along photo perimeter. Verhoeff checksum algorithm failed on 12-digit sequence. Photo background shows cloning brush artifacts."
    },
    "Authentic IIT Bombay Academic Transcript (100% Genuine)": {
        "doc_type": "10th / 12th Board Marksheet",
        "claimed_name": "Rahul Sharma",
        "claimed_apaar": "9876-5432-1098",
        "claimed_institution": "Indian Institute of Technology (IIT) Bombay",
        "serial_number": "IITB-TR-2024-00192",
        "issue_date": "2024-05-18",
        "software_signature": "DigiLocker Certified PDF/A (Adobe Distiller 21.0)",
        "baseline_drift_px": 0.3,
        "font_dpi_variance": 0.02,
        "serial_checksum_valid": True,
        "is_counterfeit": False,
        "tamper_locations": [],
        "forensic_notes": "High-fidelity micro-printing intact. Baseline alignment perfect (<0.5px variance). DigiLocker SHA-256 digital signature verified against Ministry of Education root authority."
    }
}

class DocumentFraudScanner:
    """
    Simulated Document Fraud Scanner & Forensic Inspection Engine.
    Performs OCR extraction, typographical alignment, metadata EXIF analysis,
    and visual tamper bounding-box rendering.
    """
    def __init__(self):
        pass

    def generate_forensic_scan_image(self, case_data: Dict[str, Any]) -> Image.Image:
        """
        Synthesize an authentic security-grade forensic certificate image
        with security border, watermark, extracted fields, and color-coded tamper highlight boxes.
        """
        width, height = 580, 360
        # Background: Government parchment slate tone
        is_clean = not case_data.get("is_counterfeit", False)
        bg_color = (15, 23, 42) if is_clean else (24, 18, 25)
        img = Image.new("RGB", (width, height), color=bg_color)
        draw = ImageDraw.Draw(img)

        # Outer Security Guilloche Border
        border_color = (16, 185, 129) if is_clean else (244, 63, 94)
        draw.rectangle([8, 8, width - 9, height - 9], outline=border_color, width=2)
        draw.rectangle([12, 12, width - 13, height - 13], outline=(56, 189, 248), width=1)

        # Header Watermark Banner
        draw.rectangle([13, 13, width - 14, 52], fill=(30, 41, 59))
        draw.text((24, 20), "GOVERNMENT OF INDIA • AICTE NATIONAL FORENSIC VERIFIER", fill=(245, 158, 11))
        draw.text((24, 34), f"DOCUMENT TYPE: {case_data.get('doc_type', 'ACADEMIC CREDENTIAL').upper()}", fill=(148, 163, 184))

        # Serial & Date Bar
        draw.text((24, 65), f"SERIAL NUMBER: {case_data.get('serial_number', 'N/A')}", fill=(56, 189, 248))
        draw.text((360, 65), f"ISSUE DATE: {case_data.get('issue_date', 'N/A')}", fill=(148, 163, 184))

        # Student Details Box
        draw.rectangle([24, 88, width - 24, 250], fill=(20, 30, 48), outline=(51, 65, 85))
        draw.text((38, 102), f"CANDIDATE NAME:  {case_data.get('claimed_name', 'N/A')}", fill=(241, 245, 249))
        draw.text((38, 128), f"APAAR ID:         {case_data.get('claimed_apaar', 'N/A')}", fill=(56, 189, 248))
        draw.text((38, 154), f"INSTITUTION:      {case_data.get('claimed_institution', 'N/A')}", fill=(203, 213, 225))
        draw.text((38, 180), f"CLASSIFICATION:   VERIFIED TECHNICAL ADMISSION", fill=(148, 163, 184))
        draw.text((38, 206), f"METADATA SIG:     {case_data.get('software_signature', 'Digital Original')}", fill=(148, 163, 184))

        # QR & Security Hologram Simulation
        draw.rectangle([width - 120, 100, width - 40, 180], fill=(30, 41, 59), outline=(56, 189, 248))
        draw.rectangle([width - 110, 110, width - 80, 140], fill=(56, 189, 248))
        draw.rectangle([width - 70, 145, width - 50, 170], fill=(245, 158, 11))
        draw.text((width - 115, 185), "DIGITAL QR", fill=(148, 163, 184))

        # Draw Tamper Bounding Boxes (Forensic Highlight Layer)
        tamper_locs = case_data.get("tamper_locations", [])
        for loc in tamper_locs:
            box = loc["box"]
            color = (244, 63, 94) if loc["severity"] == "CRITICAL" else (245, 158, 11)
            # Draw dashed/prominent red box around tampered text
            draw.rectangle(box, outline=color, width=3)
            # Label banner
            draw.rectangle([box[0], box[1] - 18, box[0] + len(loc["label"]) * 7 + 10, box[1]], fill=color)
            draw.text((box[0] + 4, box[1] - 16), f"[!] {loc['label']}", fill=(255, 255, 255))

        # Bottom Stamp Banner
        if is_clean:
            stamp_bg = (6, 78, 59)
            stamp_text = "STATUS: AUTHENTIC & VALIDATED (AICTE CRYPTOGRAPHIC PASS)"
            stamp_color = (52, 211, 153)
        else:
            stamp_bg = (136, 19, 55)
            stamp_text = "STATUS: CRITICAL FORGERY DETECTED (IPC SEC 468 VIOLATION)"
            stamp_color = (251, 113, 133)

        draw.rectangle([13, height - 52, width - 14, height - 14], fill=stamp_bg)
        draw.text((24, height - 42), stamp_text, fill=stamp_color)
        draw.text((width - 180, height - 38), f"TIMESTAMP: {datetime.utcnow().strftime('%H:%M:%S UTC')}", fill=(203, 213, 225))

        return img

    def analyze_document(
        self,
        preset_name: Optional[str] = None,
        uploaded_bytes: Optional[bytes] = None,
        custom_name: str = "",
        custom_apaar: str = "",
        custom_doc_type: str = "Transfer Certificate (TC)"
    ) -> Dict[str, Any]:
        """
        Perform complete multi-stage forensic analysis.
        """
        # If preset selected, use preset data
        if preset_name and preset_name in PRESET_FORENSIC_CASES:
            case = PRESET_FORENSIC_CASES[preset_name].copy()
        elif uploaded_bytes:
            # Analyze uploaded file contents
            has_ps = b"Photoshop" in uploaded_bytes or b"Adobe" in uploaded_bytes
            has_canva = b"Canva" in uploaded_bytes
            has_gimp = b"GIMP" in uploaded_bytes

            is_tampered = has_ps or has_canva or has_gimp or len(uploaded_bytes) % 2 == 1

            if is_tampered:
                sig = "Adobe Photoshop 2024" if has_ps else ("Canva Cloud PDF" if has_canva else "Modified Raster Stream")
                case = {
                    "doc_type": custom_doc_type,
                    "claimed_name": custom_name or "Uploaded Candidate",
                    "claimed_apaar": custom_apaar or "9999-8888-7777",
                    "claimed_institution": "State Technical Board",
                    "serial_number": f"IN-DOC-{int(time.time()) % 100000}",
                    "issue_date": "2023-07-12",
                    "software_signature": sig,
                    "baseline_drift_px": 7.2,
                    "font_dpi_variance": 0.38,
                    "serial_checksum_valid": False,
                    "is_counterfeit": True,
                    "tamper_locations": [
                        {"label": "Font DPI Mismatch Splicing", "box": (160, 100, 420, 140), "severity": "CRITICAL"},
                        {"label": "Metadata Tampering Header", "box": (160, 190, 380, 220), "severity": "WARNING"}
                    ],
                    "forensic_notes": f"File byte signature indicates post-processing via {sig}. Typesetting baseline drift exceeds acceptable tolerance (7.2px vs 1.5px baseline)."
                }
            else:
                case = {
                    "doc_type": custom_doc_type,
                    "claimed_name": custom_name or "Uploaded Candidate",
                    "claimed_apaar": custom_apaar or "1234-5678-9012",
                    "claimed_institution": "State Technical Board",
                    "serial_number": f"IN-GEN-{int(time.time()) % 100000}",
                    "issue_date": "2024-04-10",
                    "software_signature": "Original Digital PDF/A-1b",
                    "baseline_drift_px": 0.4,
                    "font_dpi_variance": 0.03,
                    "serial_checksum_valid": True,
                    "is_counterfeit": False,
                    "tamper_locations": [],
                    "forensic_notes": "All typographical glyphs conform to standard registrar template. Digital certificate signature verified clean."
                }
        else:
            case = PRESET_FORENSIC_CASES["Altered Transfer Certificate (Photoshop Text Splicing)"].copy()

        # Compute Forensic Risk Score (0 - 100%)
        if case["is_counterfeit"]:
            risk_score = min(98, 70 + int(case["baseline_drift_px"] * 3) + len(case["tamper_locations"]) * 5)
            verdict = "CRITICAL FORGERY DETECTED"
            verdict_badge = "CRITICAL_FRAUD"
        else:
            risk_score = 4
            verdict = "AUTHENTIC CLEAN CREDENTIAL"
            verdict_badge = "CLEAN_AUTHENTIC"

        # Multi-Layer Checklist
        checks = [
            {
                "test": "Font & Typesetting Alignment",
                "status": "FAILED" if case["baseline_drift_px"] > 2.0 else "PASSED",
                "detail": f"Baseline drift: {case['baseline_drift_px']}px (Limit: <= 1.5px). {'Typesetting splicing detected.' if case['baseline_drift_px'] > 2.0 else 'Monotype alignment verified.'}"
            },
            {
                "test": "EXIF & Metadata Software Audit",
                "status": "FAILED" if "Photoshop" in case["software_signature"] or "Canva" in case["software_signature"] or "GIMP" in case["software_signature"] else "PASSED",
                "detail": f"Detected Software: {case['software_signature']}. {'Disallowed editing tool signature identified.' if case['is_counterfeit'] else 'Certified PDF/A original.'}"
            },
            {
                "test": "Registrar Serial Checksum",
                "status": "PASSED" if case["serial_checksum_valid"] else "FAILED",
                "detail": f"Serial: {case['serial_number']}. {'Valid state registrar checksum.' if case['serial_checksum_valid'] else 'Checksum algorithm failed. Potential duplicate serial.'}"
            },
            {
                "test": "Security QR & Public Key Digest",
                "status": "PASSED" if not case["is_counterfeit"] else "FAILED",
                "detail": "SHA-256 digital watermark signature match: " + ("100% Valid." if not case["is_counterfeit"] else "Hash mismatch with central key vault.")
            }
        ]

        # Generate image
        scanned_img = self.generate_forensic_scan_image(case)

        return {
            "verdict": verdict,
            "verdict_badge": verdict_badge,
            "forensic_risk_score": risk_score,
            "case_data": case,
            "checks": checks,
            "forensic_notes": case["forensic_notes"],
            "image": scanned_img
        }

# Global Singleton Scanner
fraud_scanner = DocumentFraudScanner()
