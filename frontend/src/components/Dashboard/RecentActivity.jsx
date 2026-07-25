import { useEffect, useState } from "react";

import { getHistory } from "../../api/historyApi";

function RecentActivity() {
    const [activities, setActivities] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const loadRecentActivity = async () => {
            try {
                const data = await getHistory("", "All", 1, 3);
                setActivities(data.items ?? []);
            } catch (error) {
                console.error("Unable to load recent activity:", error);
            } finally {
                setLoading(false);
            }
        };

        loadRecentActivity();
    }, []);

    return (
        <section className="recent-card" aria-labelledby="recent-activity-title">
            <div className="recent-card-header">
                <div>
                    <p className="recent-card-eyebrow">Latest scans</p>
                    <h2 id="recent-activity-title">Recent Activity</h2>
                </div>
                <span className="recent-count">Last 3</span>
            </div>

            {loading ? (
                <p className="recent-empty">Loading recent scans...</p>
            ) : activities.length === 0 ? (
                <p className="recent-empty">No scan history available yet.</p>
            ) : (
                <div className="recent-activity-list">
                    {activities.map((activity) => {
                        const isScam = activity.prediction?.toLowerCase() === "scam";

                        return (
                            <article className="recent-activity-item" key={activity.id}>
                                <span className={`recent-status ${isScam ? "scam" : "safe"}`}>
                                    {isScam ? "Scam" : "Safe"}
                                </span>
                                <div className="recent-activity-content">
                                    <p className="recent-message">{activity.message}</p>
                                    <p className="recent-meta">
                                        {new Date(activity.created_at).toLocaleString()} · {activity.confidence}% confidence
                                    </p>
                                </div>
                            </article>
                        );
                    })}
                </div>
            )}
        </section>
    );
}

export default RecentActivity;
