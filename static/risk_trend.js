document.addEventListener("DOMContentLoaded", function () {

    const chartCanvas = document.getElementById("riskTrendChart");

    if (!chartCanvas) {
        return;
    }

    const historyData = JSON.parse(
        chartCanvas.dataset.history || "[]"
    );

    if (historyData.length === 0) {
        return;
    }

    const labels = historyData.map(function (item, index) {

        return "Assessment " + (index + 1);

    });

    const probabilities = historyData.map(function (item) {

        return item.probability;

    });

    new Chart(
        chartCanvas,
        {
            type: "line",

            data: {

                labels: labels,

                datasets: [
                    {
                        label: "Cardiovascular Risk (%)",

                        data: probabilities,

                        borderWidth: 3,

                        tension: 0.35,

                        fill: false,

                        pointRadius: 5

                    }
                ]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                scales: {

                    y: {

                        beginAtZero: true,

                        max: 100,

                        title: {

                            display: true,

                            text: "Risk Probability (%)"

                        }

                    },

                    x: {

                        title: {

                            display: true,

                            text: "Assessment"

                        }

                    }

                },

                plugins: {

                    legend: {

                        display: true

                    },

                    tooltip: {

                        callbacks: {

                            label: function (context) {

                                return (
                                    "Risk: "
                                    + context.parsed.y
                                    + "%"
                                );

                            }

                        }

                    }

                }

            }

        }
    );

});