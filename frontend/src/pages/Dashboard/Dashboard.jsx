import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import { getProfile } from "../../api/authApi";
import {getToken,removeToken,} from "../../services/tokenService";
import { getDashboardSummary }from "../../api/dashboardApi";
import {getWeeklyTrend}from "../../api/dashboardApi";
import {getScamCategories} from "../../api/dashboardApi";

import "./Dashboard.css";

import SummaryCard from "../../components/Dashboard/SummaryCard";
import ChartSection from "../../components/Dashboard/ChartSection";
import RecentActivity from "../../components/Dashboard/RecentActivity";
import WeeklyTrendChart from "../../components/Dashboard/WeeklyTrendChart";
import PieChart from "../../components/Dashboard/PieChart";







function Dashboard() {

    const [user, setUser] = useState(null);
    const [isProfileOpen, setIsProfileOpen] = useState(false);

    const [summary, setSummary] = useState({

        total_scans: 0,
        scam_detected: 0,
        safe_messages: 0,
        success_rate: 0

    });


    const [trend,setTrend] = useState([]);
    const [categories,setCategories]=useState([]);

    const navigate = useNavigate();


    useEffect(() => {

    loadProfile();

    loadSummary();

    loadTrend();

    loadCategories();

}, []);

    // useEffect(()=>{
    //     getScamCategory()
    //     .then(data=>{
    //         setCategoryData(data);
    //     });

    // },[]);



    const loadProfile = async () => {

        try {

            const data = await getProfile(getToken());

            setUser(data);

        }
        catch(error){

            console.error(error);

        }

    };



    const loadSummary = async () => {

        try {

            const data = await getDashboardSummary();

            setSummary(data);

        }
        catch(error){

            console.log(error);

        }

    };



    const loadTrend = async()=>{

        try{

            const data = await getWeeklyTrend();

            console.log("Trend API:",data);

            setTrend(data);

        }
        catch(error){

            console.error(error);

        }

    };
    const loadCategories = async()=>{

    try{

        const data = await getScamCategories();

        console.log("Categories:",data);

        setCategories(data);

    }
    catch(error){

        console.error(error);

    }

};



    const logout = () => {

        removeToken();

        navigate("/",{
            replace:true
        });

    };

    const sidebarLinks = [
        { label: "Dashboard", path: "/dashboard" },
        { label: "Scan Message", path: "/scan-message" },
        { label: "Scan Image", path: "/ocr" },
        { label: "Voice Agent", path: "/voice" },
        { label: "Chat Bot", path: "/chat-assistant" },
        { label: "Financial Literacy", path: "/financial-literacy" },
        { label: "Emergency Help", path: "/emergency" },
        { label: "History", path: "/history" },
    ];



    if(!user){

        return (

            <h2 className="loading">
                Loading...
            </h2>

        );

    }



    return (

        <div className="dashboard-page">


            <aside className="dashboard-sidebar">


                <div className={`dashboard-card profile-card ${isProfileOpen ? "is-open" : ""}`}>


                    <button
                        className="profile-toggle"
                        type="button"
                        aria-expanded={isProfileOpen}
                        onClick={() => setIsProfileOpen((isOpen) => !isOpen)}
                    >
                        👤 Profile
                        <span className="profile-chevron" aria-hidden="true">
                            {isProfileOpen ? "⌃" : "⌄"}
                        </span>
                    </button>


                    <div className="profile-item">

                        <span>Email</span>

                        <p>{user.email}</p>

                    </div>


                    <div className="profile-item">

                        <span>Phone</span>

                        <p>{user.phone}</p>

                    </div>


                    <div className="profile-item">

                        <span>Language</span>

                        <p>{user.language}</p>

                    </div>


                </div>

                <nav className="sidebar-navigation" aria-label="Dashboard navigation">
                    {sidebarLinks.map(({ label, path }) => (
                        <button
                            key={path}
                            className={`sidebar-link ${path === "/dashboard" ? "active" : ""}`}
                            type="button"
                            onClick={() => navigate(path)}
                        >
                            {label}
                        </button>
                    ))}
                </nav>

            </aside>



            <main className="dashboard-main">



                <div className="dashboard-header">


                    <div>

                        <h1 className="dashboard-title">

                            Welcome back, {user.full_name}

                        </h1>


                        <p className="dashboard-subtitle">

                            Monitor your scam detection analytics.

                        </p>


                    </div>



                    <div className="dashboard-actions">
                        <button
                            className="logout-btn"
                            onClick={logout}
                        >
                            Logout
                        </button>
                    </div>


                </div>




                <div className="summary-grid">


                    <SummaryCard
                        title="Total Scans"
                        value={summary.total_scans}
                    />


                    <SummaryCard
                        title="Scam"
                        value={summary.scam_detected}
                    />


                    <SummaryCard
                        title="Safe"
                        value={summary.safe_messages}
                    />


                    <SummaryCard
                        title="Success"
                        value={`${summary.success_rate}%`}
                    />


                </div>





                <div className="charts-grid">


                    <div className="chart-card">


                        <h2>
                            Weekly Scan Trend
                        </h2>

                        {
                            trend.length > 0 ?

                            <WeeklyTrendChart trend={trend}/>

                            :

                            <p>No scan data available</p>

                            }

                        

                    </div>



                <PieChart
                title="Scam Categories"
                categories={categories}
            />

                    {/* <ChartSection
                        title="Scam Categories"
                    /> */}



                </div>





                <RecentActivity />



            </main>


        </div>

    );

}


export default Dashboard;
