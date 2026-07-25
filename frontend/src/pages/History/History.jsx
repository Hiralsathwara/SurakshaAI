import { useEffect, useState } from "react";

import { useNavigate } from "react-router-dom";

import {
    getHistory,
    deleteHistory,
} from "../../api/historyApi";

import "./History.css";

function History() {
    const navigate = useNavigate();

    // ==========================================================
    // State Variables
    // ==========================================================

    const [history, setHistory] = useState([]);
    const [loading, setLoading] = useState(true);

    // Search & Filter
    const [search, setSearch] = useState("");
    const [debouncedSearch, setDebouncedSearch] = useState("");
    const [prediction, setPrediction] = useState("All");

    // Pagination
    const [page, setPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);
    const [totalRecords, setTotalRecords] = useState(0);


    // ==========================================================
    // Load History
    // Runs whenever:
    // • Search changes
    // • Filter changes
    // • Page changes
    // ==========================================================

    useEffect(() => {
        loadHistory();
    }, [debouncedSearch, prediction, page]);


    // ==========================================================
    // Reset Page
    // Return to page 1 whenever search/filter changes
    // ==========================================================

    useEffect(() => {
        setPage(1);
    }, [debouncedSearch, prediction]);


    // ==========================================================
    // Debounced Search
    // Wait 500ms before calling the API
    // ==========================================================

    useEffect(() => {

        const timer = setTimeout(() => {
            setDebouncedSearch(search);
        }, 500);

        return () => clearTimeout(timer);

    }, [search]);


    // ==========================================================
    // Fetch Scan History
    // ==========================================================

    const loadHistory = async () => {

        try {

            const data = await getHistory(
                debouncedSearch,
                prediction,
                page
            );

            setHistory(data.items);
            setTotalPages(data.total_pages);
            setTotalRecords(data.total);

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);

        }

    };


    // ==========================================================
    // Delete Scan History
    // ==========================================================

    const handleDelete = async (historyId) => {

        const confirmDelete = window.confirm(
            "Are you sure you want to delete this scan history?"
        );

        if (!confirmDelete) return;

        try {

            await deleteHistory(historyId);

            // Reload Updated History
            loadHistory();

        } catch (error) {

            console.error(error);

            alert("Unable to delete history.");

        }

    };


    // ==========================================================
    // Pagination Calculations
    // ==========================================================

    const PAGE_SIZE = 10;

    const pageNumbers = [];

    for (let i = 1; i <= totalPages; i++) {
        pageNumbers.push(i);
    }

    const startRecord =
        totalRecords === 0
            ? 0
            : (page - 1) * PAGE_SIZE + 1;

    const endRecord = Math.min(
        page * PAGE_SIZE,
        totalRecords
    );


    // ==========================================================
    // Loading Screen
    // ==========================================================

    if (loading) {
        return <h2>Loading History...</h2>;
    }


    // ==========================================================
    // UI
    // ==========================================================

    return (

        <div className="history-page">

           {/* ======================================================
                Page Heading
            ======================================================= */}

                <div className="history-header">

                    <button
                        className="page-back-button"
                        onClick={() => navigate("/dashboard")}
                    >
                        ← Back
                    </button>

                    <h1>
                        Scan History
                    </h1>

                </div>


            {/* ======================================================
                        Search + Filter Toolbar
            ======================================================= */}

            <div className="history-toolbar">

                <input
                    type="text"
                    placeholder="🔍 Search messages..."
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    className="search-box"
                />

                <select
                    value={prediction}
                    onChange={(e) => setPrediction(e.target.value)}
                    className="filter-select"
                >
                    <option value="All">All</option>
                    <option value="Scam">Scam</option>
                    <option value="Safe">Safe</option>
                </select>

            </div>


            {/* ======================================================
                        Records Counter
            ======================================================= */}

            <p className="records-counter">

                Showing {startRecord} - {endRecord} of {totalRecords} scans

            </p>


            {/* ======================================================
                        Scan History Cards
            ======================================================= */}

            {history.length === 0 ? (

                <p>No scan history found.</p>

            ) : (

                history.map((scan) => (

                    <div
                        key={scan.id}
                        className="history-card"
                    >

                        {/* Prediction */}

                        <h3>

                            {scan.prediction === "Scam"
                                ? "🚨 Scam"
                                : "✅ Safe"}

                        </h3>


                        {/* Original Message */}

                        <p>

                            <strong>Message:</strong>

                            {scan.message}

                        </p>


                        {/* Confidence */}

                        <p>

                            <strong>Confidence:</strong>

                            {scan.confidence}%

                        </p>


                        {/* Scan Date */}

                        <p>

                            <strong>Date:</strong>{" "}

                            {new Date(
                                scan.created_at
                            ).toLocaleString()}

                        </p>


                        {/* Delete Button */}

                        <button
                            className="delete-btn"
                            onClick={() => handleDelete(scan.id)}
                        >
                            🗑 Delete
                        </button>

                    </div>

                ))

            )}


            {/* ======================================================
                            Pagination
            ======================================================= */}

            {totalPages > 1 && (

                <div className="pagination">

                    {/* Previous Button */}

                    <button
                        className="page-btn"
                        disabled={page === 1}
                        onClick={() => setPage(page - 1)}
                    >
                        ← Previous
                    </button>


                    {/* Page Numbers */}

                    <div className="page-numbers">

                        {pageNumbers.map((number) => (

                            <button
                                key={number}
                                onClick={() => setPage(number)}
                                className={
                                    page === number
                                        ? "page-number active"
                                        : "page-number"
                                }
                            >
                                {number}
                            </button>

                        ))}

                    </div>


                    {/* Next Button */}

                    <button
                        className="page-btn"
                        disabled={page === totalPages}
                        onClick={() => setPage(page + 1)}
                    >
                        Next →
                    </button>

                </div>

            )}

        </div>

    );

}

export default History;
