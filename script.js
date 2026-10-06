function showSection(sectionName) {

    document.getElementById("hospital").style.display = "none";
    document.getElementById("pharmacy").style.display = "none";
    document.getElementById("blood").style.display = "none";

    document.getElementById(sectionName).style.display = "block";
}


async function searchHospital() {

    const name = document.getElementById("hospitalSearch").value;

    const response = await fetch("/api/hospitals?name=" + encodeURIComponent(name));

    const data = await response.json();

    let result = "";

    data.forEach(function(hospital) {

        result += `
            <div>
                <h3>🏥 ${hospital.name}</h3>
                <p>Total Beds: ${hospital.beds}</p>
                <p>Hospital Number: ${hospital.phone}</p>
                <p>Emergency Number: ${hospital.emergency}</p>
                <p>Ambulance Number: ${hospital.ambulance}</p>
            </div>
            <hr>
        `;
    });

    document.getElementById("hospitalResult").innerHTML = result;
}