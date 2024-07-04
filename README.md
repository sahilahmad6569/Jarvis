# Jarvis Voice Assistant

Jarvis is a personal voice assistant that can perform various tasks like fetching the weather, searching Wikipedia, opening websites, taking notes, and more. It's built using Python and integrates multiple libraries and APIs to provide a seamless voice-controlled experience.

## Features

- **Voice Activation:** Listens for the wake word "Jarvis" to activate.
- **Weather Information:** Fetches current weather information for a specified city.
- **Time and Date:** Tells the current time and date.
- **Wikipedia Search:** Searches Wikipedia and reads a brief summary.
- **Web Browsing:** Opens specified websites like Google, LinkedIn, GitHub, YouTube, and more.
- **Note Taking:** Takes notes and saves them to a file.
- **System Control:** Can shut down, restart, or log out of the system.
- **Generative AI Responses:** Uses Google's Generative AI to respond to general queries.

## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/sahilahmad6569/Jarvis.git
   cd Jarvis
   ```

2. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Set Environment Variables:**

   Ensure you have the following environment variables set:

   ```sh
   export GEMINI_API_KEY=your_gemini_api_key
   export WEATHER_API_KEY=your_weather_api_key
   ```

4. **Run the Application:**

   ```sh
   python main.py
   ```

## Usage

Once the application is running, it will continuously listen for the wake word "Jarvis". Once activated, you can give commands such as:

- "What's the weather?"
- "Open Google"
- "Tell me the time"
- "Search Wikipedia for Python programming"
- "Take note: Buy groceries"
- "Shutdown the system"

## Project Structure

- `main.py`: Main application script.
- `requirements.txt`: List of Python dependencies.
- `notes.txt`: File where notes are stored.

## Dependencies

- `speech_recognition`: For converting speech to text.
- `pyttsx3`: For converting text to speech.
- `google-generativeai`: For generative AI responses.
- `requests`: For making HTTP requests (used for weather API).
- `wikipedia`: For fetching Wikipedia summaries.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

**Note:** Ensure that you have valid API keys for Gemini and OpenWeatherMap services.

## Authors

- [Sahil Ahmad](https://github.com/sahilahmad6569)

## Acknowledgments

- Inspired by the idea of creating a personal voice assistant.
- Thanks to the developers of the libraries and APIs used in this project.