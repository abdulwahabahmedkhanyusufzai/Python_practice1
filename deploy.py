import subprocess
import sys

def run_cmd(cmd,check=True,capture=True,):
    """Pass cmd as a list for better security"""
    try:

        result = subprocess.run(cmd,check=check,capture_output=capture,text=True)
        return result.stdout.strip() if capture else None

    except subprocess.CalledProcessError as e:
        print(f"Error during: {' '.join(cmd)}")
        sys.exit(1)

def main():
    print("Fetching updates...")
    
    """fetching old commits"""
    old_commit = run_cmd(["git", "rev-parse", "HEAD"], capture=True)
    
    """fetching new pull"""
    print("Pulling Latest Changes from git")
    run_cmd(["git", "pull"])
    
    """fetching new commits"""
    new_commit = run_cmd(["git", "rev-parse", "HEAD"], capture=True)

    """comparing commits"""
    if old_commit == new_commit:
        print("✅ Already up to date. No build needed.")
        # Optional: still restart if you really want to, but usually not needed
        return
    """if everything goes fine we are making the build"""
    print("🏗️ New changes detected. Starting build...")
    run_cmd(["npm", "run", "build"])

    """Restarting process"""
    print("🚀 Restarting Process...")
    run_cmd(["pm2", "restart", "zeno"])

    """Deployment complete zeno"""
    print("📋 Deployment Complete. Tailing logs...")
    run_cmd(["pm2", "logs", "zeno", "--lines", "20"])


if __name__ == "__main__":
    main()
