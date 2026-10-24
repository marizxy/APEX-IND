"""
AICTE National College & Program Registry Catalog
Production-grade directory of Premier Indian Institutions, State Universities, and AICTE Programs.
"""

INSTITUTIONS_CATALOG = {
    # --- IITs (Institutes of National Importance) ---
    "Indian Institute of Technology (IIT) Madras": {
        "id": "AICTE-IIT-MDS-001",
        "type": "Institute of National Importance",
        "state": "Tamil Nadu",
        "intake_limit": 1200
    },
    "Indian Institute of Technology (IIT) Bombay": {
        "id": "AICTE-IIT-BOM-002",
        "type": "Institute of National Importance",
        "state": "Maharashtra",
        "intake_limit": 1350
    },
    "Indian Institute of Technology (IIT) Delhi": {
        "id": "AICTE-IIT-DEL-003",
        "type": "Institute of National Importance",
        "state": "Delhi",
        "intake_limit": 1250
    },
    "Indian Institute of Technology (IIT) Kharagpur": {
        "id": "AICTE-IIT-KGP-004",
        "type": "Institute of National Importance",
        "state": "West Bengal",
        "intake_limit": 1400
    },
    "Indian Institute of Technology (IIT) Kanpur": {
        "id": "AICTE-IIT-KNP-005",
        "type": "Institute of National Importance",
        "state": "Uttar Pradesh",
        "intake_limit": 1100
    },
    "Indian Institute of Technology (IIT) Roorkee": {
        "id": "AICTE-IIT-ROO-006",
        "type": "Institute of National Importance",
        "state": "Uttarakhand",
        "intake_limit": 1150
    },
    "Indian Institute of Technology (IIT) Guwahati": {
        "id": "AICTE-IIT-GHY-007",
        "type": "Institute of National Importance",
        "state": "Assam",
        "intake_limit": 950
    },
    "Indian Institute of Technology (IIT) Hyderabad": {
        "id": "AICTE-IIT-HYD-008",
        "type": "Institute of National Importance",
        "state": "Telangana",
        "intake_limit": 850
    },
    "Indian Institute of Technology (BHU) Varanasi": {
        "id": "AICTE-IIT-BHU-009",
        "type": "Institute of National Importance",
        "state": "Uttar Pradesh",
        "intake_limit": 1300
    },
    "Indian Institute of Science (IISc) Bangalore": {
        "id": "AICTE-IISC-BLR-000",
        "type": "Institute of Eminence / Research Apex",
        "state": "Karnataka",
        "intake_limit": 450
    },
    
    # --- NITs (National Institutes of Technology) ---
    "National Institute of Technology (NIT) Tiruchirappalli": {
        "id": "AICTE-NIT-TRY-101",
        "type": "National Institute of Technology",
        "state": "Tamil Nadu",
        "intake_limit": 1050
    },
    "National Institute of Technology Karnataka (NITK) Surathkal": {
        "id": "AICTE-NIT-SRT-102",
        "type": "National Institute of Technology",
        "state": "Karnataka",
        "intake_limit": 980
    },
    "National Institute of Technology (NIT) Warangal": {
        "id": "AICTE-NIT-WAR-103",
        "type": "National Institute of Technology",
        "state": "Telangana",
        "intake_limit": 1000
    },
    "National Institute of Technology (NIT) Rourkela": {
        "id": "AICTE-NIT-ROU-104",
        "type": "National Institute of Technology",
        "state": "Odisha",
        "intake_limit": 1100
    },
    "Motilal Nehru National Institute of Technology (MNNIT) Allahabad": {
        "id": "AICTE-NIT-ALD-105",
        "type": "National Institute of Technology",
        "state": "Uttar Pradesh",
        "intake_limit": 950
    },
    "National Institute of Technology (NIT) Calicut": {
        "id": "AICTE-NIT-CAL-106",
        "type": "National Institute of Technology",
        "state": "Kerala",
        "intake_limit": 1100
    },
    "National Institute of Technology (NIT) Silchar": {
        "id": "AICTE-NIT-SIL-107",
        "type": "National Institute of Technology",
        "state": "Assam",
        "intake_limit": 850
    },

    # --- Central & Premier State Universities ---
    "Anna University (CEG Campus), Chennai": {
        "id": "AICTE-UNIV-ANNA-201",
        "type": "State Technological University",
        "state": "Tamil Nadu",
        "intake_limit": 1500
    },
    "Faculty of Technology, University of Delhi": {
        "id": "AICTE-UNIV-DU-202",
        "type": "Central University",
        "state": "Delhi",
        "intake_limit": 720
    },
    "Delhi Technological University (DTU), New Delhi": {
        "id": "AICTE-UNIV-DTU-207",
        "type": "State Unitary Technical University",
        "state": "Delhi",
        "intake_limit": 2400
    },
    "Netaji Subhas University of Technology (NSUT), New Delhi": {
        "id": "AICTE-UNIV-NSUT-208",
        "type": "State Unitary Technical University",
        "state": "Delhi",
        "intake_limit": 1800
    },
    "Jawaharlal Nehru Technological University (JNTU) Hyderabad": {
        "id": "AICTE-UNIV-JNTU-203",
        "type": "State Technological University",
        "state": "Telangana",
        "intake_limit": 1200
    },
    "Visvesvaraya Technological University (VTU) Belagavi": {
        "id": "AICTE-UNIV-VTU-204",
        "type": "State Technological University",
        "state": "Karnataka",
        "intake_limit": 1300
    },
    "COEP Technological University, Pune": {
        "id": "AICTE-UNIV-COEP-205",
        "type": "State Unitary Technical University",
        "state": "Maharashtra",
        "intake_limit": 860
    },
    "Jadavpur University (Faculty of Engineering), Kolkata": {
        "id": "AICTE-UNIV-JU-206",
        "type": "State Premier University",
        "state": "West Bengal",
        "intake_limit": 900
    },

    # --- Top Engineering & Research Institutes ---
    "Birla Institute of Technology and Science (BITS) Pilani": {
        "id": "AICTE-BITS-PIL-301",
        "type": "Deemed University / Institute of Eminence",
        "state": "Rajasthan",
        "intake_limit": 1100
    },
    "International Institute of Information Technology (IIIT) Hyderabad": {
        "id": "AICTE-IIIT-HYD-306",
        "type": "Autonomous Deemed University",
        "state": "Telangana",
        "intake_limit": 500
    },
    "International Institute of Information Technology (IIIT) Bangalore": {
        "id": "AICTE-IIIT-BLR-307",
        "type": "Autonomous Deemed University",
        "state": "Karnataka",
        "intake_limit": 450
    },
    "Vellore Institute of Technology (VIT) Vellore": {
        "id": "AICTE-VIT-VEL-302",
        "type": "Deemed University / Institute of Eminence",
        "state": "Tamil Nadu",
        "intake_limit": 2200
    },
    "PSG College of Technology, Coimbatore": {
        "id": "AICTE-PSG-CBE-303",
        "type": "Govt-Aided Autonomous Institution",
        "state": "Tamil Nadu",
        "intake_limit": 840
    },
    "SRM Institute of Science and Technology, Kattankulathur": {
        "id": "AICTE-SRM-KTR-304",
        "type": "Deemed University",
        "state": "Tamil Nadu",
        "intake_limit": 1800
    },
    "Thapar Institute of Engineering and Technology, Patiala": {
        "id": "AICTE-THP-PTL-305",
        "type": "Deemed University",
        "state": "Punjab",
        "intake_limit": 1200
    },
    "R.M.D. Engineering College, Tiruvallur": {
        "id": "AICTE-ENG-001",
        "alt_id": "AICTE-ENG-RMD-401",
        "type": "Affiliated Autonomous Engineering College",
        "state": "Tamil Nadu",
        "intake_limit": 720
    },
    "Saveetha Engineering College, Chennai": {
        "id": "AICTE-ENG-SEC-402",
        "type": "Affiliated Autonomous Engineering College",
        "state": "Tamil Nadu",
        "intake_limit": 660
    },
    "Vel Tech Rangarajan Dr. Sagunthala R&D Institute": {
        "id": "AICTE-ENG-VEL-403",
        "type": "Deemed University",
        "state": "Tamil Nadu",
        "intake_limit": 900
    }
}

PROGRAMS_CATALOG = [
    "B.Tech - Computer Science & Engineering (CSE)",
    "B.Tech - Artificial Intelligence & Data Science (AI & DS)",
    "B.Tech - Electronics & Communication Engineering (ECE)",
    "B.Tech - Information Technology (IT)",
    "B.Tech - Electrical & Electronics Engineering (EEE)",
    "B.Tech - Mechanical Engineering",
    "B.Tech - Civil & Structural Engineering",
    "B.Tech - Robotics & Automation",
    "B.Tech - Biotechnology & Biochemical Engineering",
    "B.Tech - Chemical Engineering",
    "M.Tech - Advanced Computing & Cybersecurity",
    "Master of Computer Applications (MCA)",
    "Master of Business Administration (MBA - Tech Management)"
]

STUDENT_CATEGORIES = [
    "General / Open Merit",
    "Regular (Central/State Quota)",
    "NRI / Foreign National",
    "Supernumerary / EWS Quota",
    "PMSSS (Prime Minister's Special Scheme)",
    "Institutional Management Quota"
]
