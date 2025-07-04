# Installation Guide for Construction PMIS App

## Prerequisites

1.  **Frappe Bench**: You need a working Frappe Bench installation. This app is intended for ERPNext v14.
    *   If you don't have one, follow the official Frappe Bench installation guide: [https://frappeframework.com/docs/user/en/bench/installation](https://frappeframework.com/docs/user/en/bench/installation)
2.  **Git**: Required to download the app.

## Steps

1.  **Navigate to your Bench Directory**:
    Open your terminal and go to your Frappe Bench directory.
    ```bash
    cd ~/frappe-bench  # Replace with your actual bench path if different
    ```

2.  **Download the App**:
    Use `bench get-app` to download the `construction_pmis` app from its Git repository.
    *(Initially, you'll be working with a local directory. Once you push it to GitHub/GitLab, you'll use the repository URL.)*

    If your app is in a local directory (e.g., `/path/to/your/PMIS`):
    ```bash
    bench get-app /path/to/your/PMIS
    ```
    If your app is on GitHub (replace with your actual URL after pushing):
    ```bash
    # bench get-app https://github.com/[your-github-username]/PMIS.git
    ```

3.  **Install the App on Your Site**:
    Replace `[your-site-name]` with the name of the Frappe site you want to install the app on.
    ```bash
    bench --site [your-site-name] install-app construction_pmis
    ```

4.  **Migrate Your Site (if necessary)**:
    It's good practice to run migrate after installing a new app.
    ```bash
    bench --site [your-site-name] migrate
    ```

5.  **Restart Bench (if necessary)**:
    Sometimes a restart is needed for all changes to take effect.
    ```bash
    bench restart
    ```

Your `construction_pmis` app should now be installed and accessible in your ERPNext site. You can find its module and DocTypes in the system.

## Development

If you are developing this app:

1.  Enable developer mode on your site:
    ```bash
    bench --site [your-site-name] set-config developer_mode 1
    ```
2.  Make your changes in the `PMIS/construction_pmis` directory.
3.  After making changes to DocTypes or other model files, run:
    ```bash
    bench --site [your-site-name] migrate
    ```
4.  For UI changes or Python code changes that don't involve database schema, a `bench restart` might be sufficient.

## Troubleshooting

*   If you encounter issues, check the bench logs (`logs/` directory in your `frappe-bench` folder).
*   Ensure all dependencies listed in `requirements.txt` (if any beyond Frappe/ERPNext) are compatible with your environment.
