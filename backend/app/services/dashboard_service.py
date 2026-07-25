"""
===========================================================
                Dashboard Service
===========================================================

Provides dashboard analytics:

• Summary Statistics
• Weekly Scan Trend

===========================================================
"""

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.scan_history import ScanHistory




class DashboardService:

    # =====================================================
    # Dashboard Summary
    # =====================================================
    # Returns:
    # • Total Scans
    # • Scam Detected
    # • Safe Messages
    # • Success Rate
    # =====================================================

    def get_summary(
        self,
        db: Session,
        user_id: int
    ):

        scans = (
            db.query(ScanHistory)
            .filter(
                ScanHistory.user_id == user_id
            )
            .all()
        )

        total = len(scans)

        scam = sum(
            1
            for scan in scans
            if scan.prediction == "Scam"
        )

        safe = sum(
            1
            for scan in scans
            if scan.prediction == "Safe"
        )

        success_rate = (
            (safe / total) * 100
            if total > 0
            else 0
        )

        return {

            "total_scans": total,

            "scam_detected": scam,

            "safe_messages": safe,

            "success_rate": round(
                success_rate,
                2
            )

        }

    # =====================================================
    # Weekly Scan Trend
    # =====================================================
    # Returns:
    # [
    #   {
    #       "date": "2026-07-20",
    #       "count": 12
    #   }
    # ]
    # =====================================================

    def get_weekly_trend(
        self,
        db: Session,
        user_id: int
    ):

        results = (

            db.query(

                func.date(
                    ScanHistory.created_at
                ),

                func.count(
                    ScanHistory.id
                )

            )

            .filter(
                ScanHistory.user_id == user_id
            )

            .group_by(
                func.date(
                    ScanHistory.created_at
                )
            )

            .order_by(
                func.date(
                    ScanHistory.created_at
                )
            )

            .all()

        )

        return [

            {

                "date": str(date),

                "count": count

            }

            for date, count in results

        ]

    # =====================================================
    # Scam Category Distribution
    # =====================================================

    def get_scam_categories(
        self,
        db: Session,
        user_id: int
    ):

        result = (

            db.query(

                ScanHistory.prediction,

                func.count(
                    ScanHistory.id
                )

            )

            .filter(

                ScanHistory.user_id == user_id

            )

            .group_by(

                ScanHistory.prediction

            )

            .all()

        )


        return [

            {

                "category": row[0],

                "count": row[1]

            }

            for row in result

        ]
    


# =====================================================
# Service Instance
# =====================================================

dashboard_service = DashboardService()