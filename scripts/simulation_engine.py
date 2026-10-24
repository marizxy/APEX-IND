"""
AICTE National Policy "What-If" Simulation Sandbox (v5.0)
Econometric forecasting & predictive machine learning engine.
Simulates impacts of seat quota shifts, tuition fee caps, scholarship DBT multipliers,
and academic warning thresholds on national student retention, enrollments, and state exchequer.
"""

import numpy as np
import pandas as pd
from typing import Dict, Any, List

class PolicySimulationEngine:
    """
    Predictive Policy Forecasting & Econometric Simulation Sandbox.
    """
    def __init__(self):
        # Baseline National Parameters (representative of AICTE Indian Engineering Ecosystem)
        self.baseline_national_intake = 1450000
        self.baseline_national_enrolled = 1220000
        self.baseline_dropout_rate = 13.8  # percentage
        self.baseline_fee_cap = 150000     # INR per year
        self.baseline_scholarship_mult = 1.0
        self.baseline_attendance_threshold = 75.0
        self.baseline_fiscal_budget_cr = 4250.0 # INR Crores

    def run_simulation(
        self,
        intake_pct_change: float = 0.0,       # -30% to +50%
        fee_cap_inr: float = 150000.0,        # 50,000 to 300,000
        scholarship_mult: float = 1.0,        # 0.5 to 2.0x
        attendance_threshold: float = 75.0,    # 60% to 85%
        ews_expansion_pct: float = 0.0        # 0% to 15%
    ) -> Dict[str, Any]:
        """
        Execute econometric simulation pipeline and compute projected deltas.
        """
        # 1. Projected Intake Capacity
        sim_intake = int(self.baseline_national_intake * (1.0 + (intake_pct_change / 100.0)) * (1.0 + (ews_expansion_pct / 100.0)))

        # 2. Price & Capacity Elasticity of Enrollment Demand
        fee_ratio = self.baseline_fee_cap / max(50000.0, fee_cap_inr)
        demand_elasticity = (fee_ratio ** 0.28) * (scholarship_mult ** 0.18)
        sim_enrolled = int(min(sim_intake, self.baseline_national_enrolled * (1.0 + (intake_pct_change / 100.0) * 0.65) * demand_elasticity))

        # 3. Predictive Dropout & Attrition Rate (%)
        # Higher fee increases dropout stress; higher scholarship reduces dropout stress;
        # higher attendance threshold improves early remedial intervention.
        fee_stress_factor = (fee_cap_inr / self.baseline_fee_cap) ** 0.32
        scholarship_relief_factor = (1.0 / max(0.4, scholarship_mult)) ** 0.40
        remedial_factor = 1.0 - ((attendance_threshold - 70.0) * 0.007)

        sim_dropout = max(3.5, min(28.0, self.baseline_dropout_rate * fee_stress_factor * scholarship_relief_factor * remedial_factor))

        # 4. Vacant Seats & Capacity Utilization (%)
        sim_vacant_seats = max(0, sim_intake - sim_enrolled)
        sim_vacancy_pct = (sim_vacant_seats / sim_intake) * 100.0 if sim_intake else 0
        baseline_vacancy_pct = ((self.baseline_national_intake - self.baseline_national_enrolled) / self.baseline_national_intake) * 100.0

        # 5. Fiscal Exchequer Budget Impact (INR Crores)
        sim_fiscal_cr = round(self.baseline_fiscal_budget_cr * scholarship_mult * (sim_enrolled / self.baseline_national_enrolled), 1)

        # 6. Ghost Proxy Risk Index (0 - 100)
        # When seat expansion exceeds 25% with low scholarship funding, ghost seat risk spikes
        proxy_risk = int(max(5, min(95, 12 + max(0, intake_pct_change * 0.8) + (2.0 - scholarship_mult) * 15 + max(0, (fee_cap_inr - 180000) / 4000))))

        # 7. Tier-Wise Comparative Breakdown (for Plotly Grouped Bar Chart)
        tiers = [
            "IITs & Institutes of National Importance",
            "NITs & Central Universities",
            "State Government Engineering Colleges",
            "Autonomous Accredited Institutes",
            "Affiliated Private Technical Colleges"
        ]
        base_tier_enrolled = [32000, 78000, 290000, 410000, 410000]
        sim_tier_enrolled = []

        for i, base_val in enumerate(base_tier_enrolled):
            # Premier institutions have inelastic demand; private colleges are highly sensitive
            elasticity_weight = 0.05 if i < 2 else (0.25 if i == 2 else 0.50)
            mult = 1.0 + (intake_pct_change / 100.0) * elasticity_weight + (demand_elasticity - 1.0) * elasticity_weight
            sim_tier_enrolled.append(int(base_val * mult))

        df_tiers = pd.DataFrame({
            "Institutional Tier": tiers,
            "Baseline Enrolled": base_tier_enrolled,
            "Simulated Enrolled": sim_tier_enrolled
        })

        # 8. Sensitivity Curve Data (Dropout Rate vs Fee Cap across Scholarship Multipliers)
        fee_range = np.linspace(60000, 280000, 10)
        sensitivity_records = []
        for f in fee_range:
            for s_mult, label in [(0.75, "0.75x (Reduced Subsidy)"), (1.0, "1.0x (Standard Baseline)"), (1.5, "1.5x (Expanded DBT)")]:
                f_factor = (f / self.baseline_fee_cap) ** 0.32
                s_factor = (1.0 / s_mult) ** 0.40
                d_rate = max(3.5, min(28.0, self.baseline_dropout_rate * f_factor * s_factor * remedial_factor))
                sensitivity_records.append({
                    "Tuition Fee Cap (₹)": int(f),
                    "Projected Dropout Rate (%)": round(d_rate, 2),
                    "Scholarship Regime": label
                })
        df_sensitivity = pd.DataFrame(sensitivity_records)

        # 9. Executive Ministry Policy Resolution Text
        dropout_delta = sim_dropout - self.baseline_dropout_rate
        enrolled_delta = sim_enrolled - self.baseline_national_enrolled
        budget_delta = sim_fiscal_cr - self.baseline_fiscal_budget_cr

        resolution_status = "RECOMMENDED FOR ADOPTION" if dropout_delta <= -1.0 and sim_vacancy_pct < 20.0 else (
            "CONDITIONAL APPROVAL REQUIRED" if dropout_delta <= 1.5 else "REJECTED (HIGH ATTRITION RISK)"
        )

        policy_brief = f"""### AICTE Executive Council Policy Resolution (Draft #{int(fee_cap_inr)%10000})
**Simulated Policy Formulation:**
- **Sanctioned Capacity Adjustment:** `{intake_pct_change:+.1f}%` ({sim_intake:,} total seats)
- **Approved Tuition Fee Ceiling:** `₹{int(fee_cap_inr):,}` per annum
- **Scholarship Direct Benefit Transfer (DBT):** `{scholarship_mult:.2f}x` multiplier
- **Early-Warning Attendance Sensitivity:** `{attendance_threshold:.1f}%`
- **Supernumerary EWS Quota Allocation:** `+{ews_expansion_pct:.1f}%`

**Algorithmic Impact Assessment:**
1. **Student Enrollment Cohort:** Projected at **{sim_enrolled:,}** students ({enrolled_delta:+,} delta vs baseline).
2. **National Attrition & Dropout Rate:** Moves from **{self.baseline_dropout_rate:.1f}%** to **{sim_dropout:.1f}%** ({dropout_delta:+.1f}% net shift).
3. **Institutional Seat Vacancy:** Projected at **{sim_vacancy_pct:.1f}%** ({sim_vacant_seats:,} vacant seats).
4. **Exchequer Fiscal Outlay:** Projected at **₹{sim_fiscal_cr:,.1f} Cr** ({budget_delta:+,.1f} Cr delta).
5. **Proxy Syndicate & Ghost Seat Risk:** Evaluated at **{proxy_risk}/100** ({'LOW' if proxy_risk < 30 else ('MODERATE' if proxy_risk < 60 else 'HIGH RISK')}).

**Regulatory Council Recommendation:**
> **VERDICT: {resolution_status}**  
> *{'The proposed parameters improve national student retention by ' + f'{-dropout_delta:.1f}% while keeping fiscal expansion within statutory reserves.' if dropout_delta < 0 else 'The policy parameters increase academic dropout risks or exchequer burden beyond sustainable thresholds. Consider raising scholarship DBT multipliers to offset tuition adjustments.'}*
"""

        return {
            "sim_intake": sim_intake,
            "sim_enrolled": sim_enrolled,
            "sim_dropout": sim_dropout,
            "sim_vacancy_pct": sim_vacancy_pct,
            "sim_fiscal_cr": sim_fiscal_cr,
            "proxy_risk": proxy_risk,
            "baseline_intake": self.baseline_national_intake,
            "baseline_enrolled": self.baseline_national_enrolled,
            "baseline_dropout": self.baseline_dropout_rate,
            "baseline_vacancy_pct": baseline_vacancy_pct,
            "baseline_fiscal_cr": self.baseline_fiscal_budget_cr,
            "df_tiers": df_tiers,
            "df_sensitivity": df_sensitivity,
            "policy_brief": policy_brief,
            "resolution_status": resolution_status
        }

# Global Singleton Policy Engine
policy_engine = PolicySimulationEngine()
