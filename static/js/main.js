function openModal() {
  const modal = document.getElementById("contactModal");
  const iframe = document.getElementById("contactFrame");

  if (modal) {
    // Reload iframe to fresh form
    if (iframe) {
      iframe.src = "/form"; // Ensure this matches your Flask route
    } else {
      console.error("Iframe not found!");
    }

    modal.style.display = "flex";
  } else {
    console.error("Modal not found!");
  }
}

function closeModal() {
  const modal = document.getElementById("contactModal");
  if (modal) {
    modal.style.display = "none";
  }
}
