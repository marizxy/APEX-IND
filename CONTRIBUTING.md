# 🤝 Contributing to AICTE Nexus India (Apex-Ind)

Thank you for your interest in contributing to **AICTE Nexus (Apex-Ind)** — the National APAAR Regulatory Command Center and Autonomous Fraud Interception Grid. This project serves as a mission-critical sovereign intelligence platform under the **Ministry of Education, Government of India**, operating under strict enterprise engineering, security, and algorithmic standards.

We welcome contributions from software architects, AI/ML researchers, security auditors, and full-stack developers. To ensure codebase stability, zero regulatory regressions, and adherence to production security standards, all contributors must adhere to the guidelines set out below.

---

## 1. Code of Conduct & Ethical Integrity

By contributing to this repository, you agree to:
* **Maintain Zero-Tolerance for Vulnerabilities:** Ensure all contributions are free of insecure dependencies, plain-text credential leaks, or non-deterministic state mutations.
* **Respect Data Privacy:** Never commit real-world personally identifiable information (PII), unmasked student records, or production API tokens. Use only mock or synthetic data compliant with the Indian Information Technology Act (2000).
* **Uphold Sovereign Digital Standards:** Align all technical implementations with the principles of the **National Education Policy (NEP 2020)** and **Academic Bank of Credits (ABC)** regulations.

---

## 2. Git Workflow & Branching Strategy

We follow a structured **Trunk-Based / Git-Flow Hybrid** model. The `main` branch is production-ready, protected, and continuously deployable.

```
       feature/gh-42-gnn-convolution
          o───o───o
         /         \  (Pull Request + CI Check)
main ───o───────────o────────────────────────────o (Release v5.1)
         \         /
          o───o───o
       fix/gh-58-merkle-collision
```

### Branch Naming Conventions
Always create feature and bugfix branches from the latest `main` branch using the following standardized prefixes:

| Branch Type | Prefix Pattern | Example |
| :--- | :--- | :--- |
| **New Feature** | `feature/<issue-number>-<short-description>` | `feature/88-gnn-temporal-convolution` |
| **Bug Fix** | `fix/<issue-number>-<short-description>` | `fix/94-session-state-dropdown-reload` |
| **Performance Optimization**| `perf/<short-description>` | `perf/sub15ms-vector-indexing` |
| **Documentation** | `docs/<short-description>` | `docs/architecture-gnn-telemetry` |
| **Refactoring** | `refactor/<module-name>` | `refactor/modular-frontend-components` |
| **Security Patch** | `security/<cve-or-description>` | `security/tls-kyber768-cipher-upgrade` |

---

## 3. Commit Message Standards (Conventional Commits)

Commit messages must adhere strictly to the [Conventional Commits v1.0.0](https://www.conventionalcommits.org/) specification. This ensures automated CHANGELOG generation and crystal-clear auditability for regulatory evaluators.

### Commit Format
```text
<type>(<optional-scope>): <concise-imperative-description>

[optional detailed body explaining WHY the change was made]

[optional footer referencing issue numbers: e.g., Closes #42]
```

### Approved Types
* `feat`: A new user-facing feature or backend engine capability.
* `fix`: A bug fix in UI state, backend persistence, or model inference.
* `perf`: A code change that improves execution speed or memory footprint (e.g., sub-15ms GNN latency).
* `refactor`: Code restructuring that neither fixes a bug nor adds a feature.
* `docs`: Documentation-only updates (README, ARCHITECTURE, docstrings).
* `test`: Adding new test suites or modifying existing unit/integration tests.
* `security`: Patches addressing cryptographic, authentication, or PII vulnerabilities.
* `chore`: Build scripts, dependencies, configuration updates (`.env.example`, `requirements.txt`).

### Examples
```bash
# Correct
git commit -m "feat(gnn): add 2-hop GraphSAGE neighborhood aggregation for proxy detection"
git commit -m "fix(frontend): resolve infinite loading spinner during batch manifest ingestion"
git commit -m "perf(rag): vectorize statutory policy search achieving 12ms retrieval"
git commit -m "security(crypto): enforce SHA-256 Merkle root verification on student manifests"

# Incorrect (will be rejected in code review)
git commit -m "updated stuff"
git commit -m "fixed bug in app.py"
git commit -m "WIP"
```

---

## 4. Local Development & Setup Workflow

### Step 1: Fork & Clone
```bash
git clone https://github.com/<your-username>/APEX-IND.git
cd APEX-IND
```

### Step 2: Initialize Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3: Install Developer Quality Tools
```bash
pip install black flake8 mypy pytest
```

### Step 4: Configure Local Environment
```bash
cp .env.example .env
```

### Step 5: Verify Local Application & Telemetry
```bash
# Launch Streamlit local instance
streamlit run frontend/app.py

# In a separate terminal, test the automated ingestion and audit pipelines
python3 scripts/batch_ingestion.py --dry-run
python3 scripts/security_audit.py
```

---

## 5. Code Quality & Architecture Guardrails

Before opening a Pull Request, verify that your code adheres to our five architectural invariants:

1. **Sub-15ms Latency Constraint:** Any modification to `backend/gnn_engine/` or `backend/rlhf_copilot/` must not degrade overall inference latency beyond **15ms** under benchmark datasets.
2. **Deterministic Cryptographic Hashing:** Never use non-deterministic serialization (e.g., standard Python `hash()` or un-ordered dict stringification) when computing Merkle leaves or SHA-256 block receipts. Always use normalized UTF-8 byte sequences.
3. **Role-Based Isolation (RBAC):** Registrar-scoped queries must never return records outside the authorized institutional node. Universal multi-tenant leakage is treated as a critical severity defect.
4. **Clean Modular Structure:** 
   - UI code belongs exclusively in `frontend/` or `frontend/components/`.
   - Core AI, cryptographic, and database models belong strictly in `backend/`.
   - Standalone CLI utilities belong in `scripts/`.
5. **Python Compilation & Typing:** Every Python file must compile with zero errors:
   ```bash
   python3 -m py_compile $(git ls-files '*.py')
   flake8 backend frontend scripts --max-line-length=120 --ignore=E501,W503
   ```

---

## 6. Pull Request (PR) Submission Guidelines

1. **Keep PRs Focused:** Submit small, self-contained PRs addressing a single feature or bug. Avoid monolithic 3,000-line diffs.
2. **Pass All CLI Audits:** Ensure `python3 scripts/security_audit.py` passes with a **100/100 Integrity Score**.
3. **Fill Out the PR Template:** Every PR must include a clear summary, testing steps, and relevant screenshots or terminal logs.

---

## 7. Pull Request Template

Copy and paste the template below into your GitHub Pull Request description:

```markdown
### 📋 Description of Changes
<!-- Provide a concise 2-3 sentence overview of what this PR introduces or fixes. -->

### 🎯 Addressed Issue
<!-- Reference the GitHub issue: e.g., Resolves #42 -->
Resolves #

### 🧪 Verification & Testing
<!-- Describe how the changes were verified locally. -->
- [ ] Successfully executed `streamlit run frontend/app.py`
- [ ] Executed `python3 scripts/security_audit.py` (100/100 score)
- [ ] Tested batch manifest ingestion with zero UI blocking
- [ ] Confirmed strict institutional node scoping (Registrar vs Central Admin)
- [ ] Verified sub-15ms GNN inference latency

### 🔒 Security & Cryptographic Compliance
- [ ] No hardcoded passwords, private keys, or API tokens introduced
- [ ] SHA-256 Merkle proof integrity maintained
- [ ] Zero unmasked student PII committed

### 📸 Visual Evidence (Screenshots / Terminal Output)
<!-- Attach screenshot of the UI or paste terminal execution logs -->
```

---

## 8. Maintainers & Governance

* **Project Architect:** Mariyon Decosta L (RMD Team)
* **Initiative:** AICTE Nexus India (Apex-Ind)
* **Sponsoring Body:** Ministry of Education, Government of India
* **Issues & Discussions:** Please open an issue on the GitHub repository for queries, design proposals, or RFC discussions.
