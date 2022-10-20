SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
#echo $SCRIPT_DIR

#only needed to pull latest version
docker pull ghcr.io/si-gen/jportal2:latest

docker run --rm -v ${SCRIPT_DIR}:/local ghcr.io/si-gen/jportal2:latest \
                      --inputdir=/local/sql/si \
                      --builtin-generator PostgresDDL:/local/generated_sources/generated_sql \
                      --template-generator SQLAlchemy:/local/generated_sources/python/jportal \
                      --download-template "SQLAlchemy:https://github.com/SI-Gen/jportal2-generator-vanguard-sqlalchemy/archive/refs/tags/1.8.zip|stripBaseDir"                      
