function searchPlaces() {
  const serviceType = document.getElementById("serviceType").value;
  const userLocation = document.getElementById("userLocation").value;
  const radius = document.getElementById("radius").value;

  if (!userLocation) {
    alert("Please enter a location.");
    return;
  }

  let searchQuery = "";
  if (serviceType === "pharmacy") {
    searchQuery = "pharmacy";
  } else if (serviceType === "veterinary") {
    searchQuery = "veterinary clinic";
  } else if (serviceType === "pet shop") {
    searchQuery = "pet shop";
  }

  const query = encodeURIComponent(`${searchQuery} near ${userLocation}`);
  const mapsUrl = `https://www.google.com/maps/search/${query}/@?radius=${radius}`;

  window.open(mapsUrl, "_blank");
}

// map.js
document.addEventListener("DOMContentLoaded", () => {
  // Only run if user came from a link with #map-section
  if (window.location.hash === "#map-section") {
    // Reset the hash so browser doesn't auto-jump
    history.replaceState(null, null, " "); 

    const mapSection = document.querySelector("#map-section");
    if (mapSection) {
      setTimeout(() => {
        mapSection.scrollIntoView({ behavior: "smooth", block: "center" });
      }, 400); // delay just for smoothness
    }
  }
});
