document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("scrape-form").addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent page reload

        let websiteUrl = document.getElementById("website_url").value.trim();
        let csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
        let outputDiv = document.getElementById("output");

        if (!websiteUrl) {
            outputDiv.innerHTML = "<p style='color: red;'>⚠️ Please enter a valid URL.</p>";
            return;
        }

        outputDiv.innerHTML = "<p>⏳ Scraping in progress...</p>"; // Show loading message

        try {
            let response = await fetch("/scrape/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken // Required for Django CSRF protection
                },
                body: JSON.stringify({ url: websiteUrl })
            });

            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }

            let data = await response.json();

            if (data.error) {
                outputDiv.innerHTML = `<p style='color: red;'>❌ ${data.error}</p>`;
            } else {
                // Format results
                outputDiv.innerHTML = `
                    <h2>✅ Scraping Results</h2>
                    <p><strong>Title:</strong> ${data.title || "N/A"}</p>
                    <p><strong>URL:</strong> <a href="${data.url}" target="_blank">${data.url}</a></p>
                    <p><strong>Category:</strong> ${data.category || "Unknown"}</p>
                    <h3>Headings:</h3>
                    <ul>${data.headings.map(h => `<li>${h}</li>`).join("") || "<li>No headings found</li>"}</ul>
                    <h3>Paragraphs:</h3>
                    <ul>${data.paragraphs.map(p => `<li>${p}</li>`).join("") || "<li>No paragraphs found</li>"}</ul>
                `;
            }
        } catch (error) {
            console.error("❌ Error:", error);
            outputDiv.innerHTML = `<p style='color: red;'>❌ Failed to scrape. Check console for details.</p>`;
        }
    });
});
