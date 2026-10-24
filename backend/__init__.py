"""
AICTE Nexus India - Backend Core Architecture
Modular AI Engines, Cryptographic Verifiers, Database Stores, and Inter-Ministerial Gateways.
"""

from pathlib import Path
import sys

# Ensure backend root is on sys.path
_BACKEND_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = _BACKEND_DIR.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
if str(_BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(_BACKEND_DIR))
