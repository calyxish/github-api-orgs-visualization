# Visualizing GitHub Organizations by Country to Assess Programming Community Growth

## 1. Description
The github-api-orgs-visualization project aims to analyze and visualize the distribution of GitHub organizations across various countries using the GitHub API.

As a software developer from Ghana, I recognized the need to understand the programming community's landscape to enhance local development. This project collects real-time data on GitHub organizations in different countries, including Ghana, to identify areas for growth and improvement in programming education and support within the local tech ecosystem.

Key features of this project include:

Real-time Data Collection: Utilizing the GitHub API to fetch the number of organizations by country.
Interactive Visualizations: Creating engaging bar charts using Plotly to effectively present the data.
Insightful Analysis: Highlighting Ghana's position relative to other countries, emphasizing the need for improved programming education and support.
This repository serves as a valuable resource for developers, educators, and stakeholders interested in assessing and fostering the growth of programming communities worldwide.


## 2. Table of Contents

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)
- [Acknowledgements](#acknowledgements)

![Project Preview](Visualizing%20GitHub%20Organizations.png)


## 3. Installation

1. Clone the repository:
   ```sh markdown
   HTTPS
   git clone https://github.com/calyxish/github-api-orgs-visualization.git

   GitHub CLI
   git clone gh repo clone calyxish/github-api-orgs-visualization

   ```
2. Navigate to the project directory
   ```sh
   cd github-api-orgs-visualization
   ```
3. Install required packages
   ```sh markdown
    pip install -r requirements.txt
   ```

## 4. Dependencies
   ```sh markdown
   requests
   plotly

   ```

## 5. Usage
Set up your GitHub Personal Access Token: Replace the placeholder in the script with your actual GitHub personal access token. This token is necessary for authentication when making API requests.
   ```sh markdown
   TOKEN = 'your_personal_access_token'
   ```
Run the script: Execute the script to gather data and create the visualization
   ```sh markdown
    python visualize github organizations.py
   ```


### How to Obtain Your GitHub Personal Access Token

###### i. Sign in to GitHub:
Go to GitHub.com and sign in to your account.

###### ii.
Go to Settings
Click on your profile picture in the upper right corner of the page and select Settings from the dropdown menu.

###### iii. Access Developer Settings:
In the left sidebar, scroll down and click on Developer settings.

###### iv. Personal Access Tokens:
Click on Personal access tokens in the left sidebar. Then, select Tokens (classic).

###### v. Generate New Token:
Click the Generate new token button.

###### vi. Configure Token:
Note: Give your token a descriptive name in the Note field (e.g., "GitHub API Access").
Expiration: Choose an expiration for your token (e.g., 30 days, 60 days, or no expiration).
Select Scopes: Choose the scopes or permissions you want to grant this token. For general API access, you may want to select:
repo (for full control of private repositories)
read:user (to read user profile data)
user (for reading and writing user profile data)

###### vii. Generate Token:
After selecting the desired scopes, click the Generate token button at the bottom of the page.

###### viii .Copy Your Token:
Your new token will be displayed on the screen. Copy it immediately, as you won’t be able to see it again. Store it securely.

###### Important Notes:
Treat your token like a password. Do not share it or expose it in your code (e.g., don't include it directly in your scripts or commit it to your repository).
If you believe your token has been compromised, you can revoke it and generate a new one.

## 6. Contributing

Guidelines for contributing to your project.

```sh markdown

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**. Thank You!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
```

## 7. License

Distributed under ... Not Yet

## 8. Contact Information
Calyx Ish
GitHub: @calyxish

## 8. Acknowledgements

```sh markdown
GitHub API for providing the necessary data.
Plotly for the interactive visualizations.

```