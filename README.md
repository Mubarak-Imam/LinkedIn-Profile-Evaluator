# LinkedIn Profile Evaluator

The LinkedIn Profile Evaluator is a web application that analyzes LinkedIn profile PDFs and provides a comprehensive evaluation, including an overall profile score, strengths, areas for improvement, and final recommendations.

## Features

- Upload your LinkedIn profile PDF
- Receive an overall profile score out of 100
- Get detailed feedback on strengths and areas for improvement
- Recommendations for enhancing your LinkedIn profile

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Mubarak-Imam/LinkedIn-Profile-Evaluator.git
    cd LinkedIn-Profile-Evaluator
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    env\Scripts\activate  # On Windows
    source env/bin/activate  # On macOS/Linux
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set your OpenAI API key as an environment variable:
    ```bash
    set OPENAI_API_KEY=your_openai_api_key  # On Windows
    export OPENAI_API_KEY=your_openai_api_key  # On macOS/Linux
    ```

5. Run the application:
    ```bash
    flask run
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Upload your LinkedIn profile PDF using the file upload form.
3. Click "Upload and Analyze" to receive your profile evaluation.

## CI/CD Pipeline

This project uses GitHub Actions for Continuous Integration (CI) and Continuous Deployment (CD). The CI pipeline runs automated tests on every push to the repository, while the CD pipeline deploys the application to Render on every push to the main branch.

### CI Pipeline

- Tool: GitHub Actions
- Trigger: Pushes to `main` and `new-feature-branch` branches, and pull requests to `main`
- Steps:
  1. Checkout code
  2. Set up Python environment
  3. Install dependencies
  4. Run tests

### CD Pipeline

- Tool: GitHub Actions
- Trigger: Pushes to `main` branch
- Steps:
  1. Checkout code
  2. Set up Python environment
  3. Install dependencies
  4. Deploy to Render

### Monitoring and Alerts

- Tool: UptimeRobot
- Metric: Uptime and Response Time
- Alerts: Email notifications for downtime or performance issues

### Deployment

- Tool: Render
- Webpage link: https://linkedin-profile-evaluator.onrender.com/

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## Contact

For any questions or issues, please contact [Mubarak Imam](https://github.com/Mubarak-Imam).

