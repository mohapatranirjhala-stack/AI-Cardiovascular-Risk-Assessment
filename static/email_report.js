function openEmailDialog() {

    document.getElementById("emailDialog").style.display = "flex";

}


function closeEmailDialog() {

    document.getElementById("emailDialog").style.display = "none";

    document.getElementById("emailStatus").innerText = "";

}


async function sendEmailReport() {

    const email =
        document.getElementById("receiverEmail").value.trim();

    const status =
        document.getElementById("emailStatus");


    if (!email) {

        status.innerText =
            "Please enter an email address.";

        return;
    }


    status.innerText =
        "Sending report...";


    try {

        const response = await fetch(
            "/email-report",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    email: email
                })
            }
        );


        const result = await response.json();


        if (result.success) {

            status.innerText =
                "✅ Report emailed successfully.";

        } else {

            status.innerText =
                "❌ " + result.message;

        }

    } catch (error) {

        console.error(error);

        status.innerText =
            "❌ Unable to send the report.";

    }

}