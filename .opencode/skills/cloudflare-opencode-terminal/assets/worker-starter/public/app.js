const button = document.querySelector("#check");
const result = document.querySelector("#result");
button.addEventListener("click", async () => {
  button.disabled = true;
  result.textContent = "Memeriksa koneksi...";
  try {
    const response = await fetch("/api/hello", {
      headers: { Accept: "application/json" },
      signal: AbortSignal.timeout(10000),
    });
    if (!response.ok) throw new Error("API_ERROR");
    const data = await response.json();
    if (typeof data.message !== "string") throw new Error("INVALID_RESPONSE");
    result.textContent = data.message;
  } catch {
    result.textContent = "Koneksi belum berhasil. Coba lagi.";
  } finally {
    button.disabled = false;
  }
});
