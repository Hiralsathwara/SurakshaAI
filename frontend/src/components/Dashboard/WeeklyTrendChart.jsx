import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Tooltip,
    Legend
} from "chart.js";

import { Line } from "react-chartjs-2";


ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Tooltip,
    Legend
);


function WeeklyTrendChart({trend}) {


    const data = {
        labels: trend.map(item => new Date(item.date).toLocaleDateString("en-US", {
            day: "numeric",
            month: "short"
        })),
        datasets: [
            {
                label: "Weekly Scans",
                data: trend.map(item => item.count ?? 0),
                borderColor: "#3b82f6",
                backgroundColor: "rgba(59, 130, 246, 0.2)",
                borderWidth: 2,
                tension: 0.4,
                fill: true,
                pointRadius: 4,
                pointHoverRadius: 6
            }
        ]
    };


    const options = {

        responsive:true,

        maintainAspectRatio:false

    };


    return (

        <div style={{height:"300px"}}>

            <Line
                data={data}
                options={options}
            />

        </div>

    );

}


export default WeeklyTrendChart;