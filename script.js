async function translateText() {
    let text = document.getElementById("inputText").value;
    let source = document.getElementById("sourceLang").value;
    let target = document.getElementById("targetLang").value;

    const url = `https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=${source}|${target}`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        document.getElementById("output").innerText =
            data.responseData.translatedText;
    } catch (error) {
        console.error("Translation Error:", error);
        document.getElementById("output").innerText =
            "Error translating text.";
    }
}
