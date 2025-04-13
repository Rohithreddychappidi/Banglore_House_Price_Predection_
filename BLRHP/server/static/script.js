// Fetch locations when the page loads
window.onload = function () {
  fetch("/Get_Location_Names")
    .then(response => response.json())
    .then(data => {
      const locations = data.Locations;
      const locationSelect = document.getElementById("location");

      locations.forEach(loc => {
        const option = document.createElement("option");
        option.text = loc;
        option.value = loc;
        locationSelect.add(option);
      });
    });
};

function predictPrice() {
  const sqft = document.getElementById("sqft").value;
  const bhk = document.getElementById("bhk").value;
  const bath = document.getElementById("bath").value;
  const location = document.getElementById("location").value;

  if (!sqft || !bhk || !bath || !location) {
    alert("Please fill in all fields.");
    return;
  }

  fetch("/predict_home_price", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      total_sqft: sqft,
      bhk: bhk,
      bath: bath,
      Location: location
    })
  })
    .then(response => response.json())
    .then(data => {
      document.getElementById("result").innerText =
        "Estimated Price: ₹ " + data.estimated_price + " Lakhs";
    });
}
