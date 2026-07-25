import { Pie } from "react-chartjs-2";

import {
    Chart as ChartJS,
    ArcElement,
    Tooltip,
    Legend
} from "chart.js";


ChartJS.register(
    ArcElement,
    Tooltip,
    Legend
);


function PieChart({title, categories}) {

    console.log("Pie Data:", categories);

    const categoryColors = categories.map(({ category }) => {
        const normalizedCategory = category.toLowerCase();

        if (normalizedCategory.includes("scam")) {
            return "#EF4444";
        }

        if (normalizedCategory.includes("safe")) {
            return "#22C55E";
        }

        return "#94A3B8";
    });

    const data = {

        labels: categories.map(
            item => item.category
        ),

        datasets:[
            {
                data: categories.map(
                    item => item.count
                ),

                backgroundColor: categoryColors,

                borderColor: "#FFFFFF",

                borderWidth:2
            }
        ]

    };


    const options = {

        responsive:true,

        maintainAspectRatio:false

    };


    return (

        <div 
            className="chart-card"
            style={{
                height:"350px"
            }}
        >

            <h2>{title}</h2>

            <Pie
                data={data}
                options={options}
            />

        </div>

    );

}


export default PieChart;
