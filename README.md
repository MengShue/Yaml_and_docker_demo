## Lookup-CLI Tool

### Overview

lookup-cli is a command-line tool that allows you to query user information stored in a YAML configuration file. It supports flexible execution both locally and in a Docker container.
- Local Usage: Uses absolute paths to locate the YAML configuration file.
- Container Usage: Uses an environment variable to dynamically specify the path to the YAML configuration file.
-----------------------------------------------------------------------------

### Prerequisites

- Python 3.10 or later (recommended to use pyenv)
- Docker and Docker Compose

Install Python with pyenv
- Install pyenv:
```shell
curl https://pyenv.run | bash
```
- Restart your shell or reload your profile:
```shell
exec $SHELL
```
- Install Python 3.10:
```shell
pyenv install 3.10.0
pyenv global 3.10.0
```
- Confirm Python version:
```shell
python --version
```
-----------------------------------------------------------------------------
### Project Structure
```shell
project-root/
├── config/
│   └── data.yaml
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yaml
├── src/
│   ├── config_reader.py
│   └── lookup-cli.py
└── requirements.txt
```
-----------------------------------------------------------------------------
### Configuration File (data.yaml)
Example YAML data:
```yaml
- name: Alice
  age: 18
  occupation: student
- name: Bob
  age: 33
  occupation: unemployed
- name: Charlie
  age: 65
- name: David
  age: 25
  occupation: software engineer
```
-----------------------------------------------------------------------------
### Local Usage
1.	Install dependencies:

```shell
pip install -r requirements.txt
```

2. Run the CLI command:

```shell
src/lookup-cli Alice age
```

3. Important Notes:

	•	The YAML file path is resolved using absolute paths in local execution.

	•	Ensure the YAML file exists in the config/ directory and is accessible.
-----------------------------------------------------------------------------
### Container Usage
#### Docker compose (docker-compose in ubuntu system)

1. Build the Docker image:
```shell
cd docker
docker compose build
```
OR
```shell
docker buildx build -t lookup-cli -f ./docker/Dockerfile .
```
2. Run the CLI command in the container:

```shell
docker compose -f docker/docker-compose.yaml up -d
docker exec -it lookup-cli-container lookup-cli Alice age
```

3. Environment Variables:

    The container uses an environment variable (CONFIG_PATH) to specify the YAML configuration file path.

4. Dynamic Configuration:

    The data.yaml file is dynamically mounted using Docker volumes, allowing modifications without rebuilding the image.

-----------------------------------------------------------------------------
### Troubleshooting
1. File Not Found Errors:
- Ensure the YAML file exists in the config/ directory locally or is mounted correctly in the container.
2. Environment Variable Issues:
- Check that the CONFIG_PATH variable is properly set inside the container:
```shell
docker compose run lookup-cli-service /bin/sh
echo $CONFIG_PATH
```
3. Permission Denied Errors:
- Ensure the lookup-cli.py file is executable:
```shell
chmod +x src/lookup-cli.py
```
