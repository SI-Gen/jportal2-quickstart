SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
#echo $SCRIPT_DIR

#only needed to pull latest version
echo "Checking for latest version of JPortal2..."
docker pull ghcr.io/si-gen/jportal2:latest
echo "Done!"

docker run --rm -v ${SCRIPT_DIR}:/local ghcr.io/si-gen/jportal2:latest \
                      --inputdir=/local/sql/si \
                      --builtin-generator PostgresDDL:/local/generated_sources/generated_sql \
                      --builtin-generator JavaJCCode:/local/generated_sources/java \
                      --template-generator SQLAlchemy:/local/generated_sources/python/jportal \
                      --download-template "SQLAlchemy:https://github.com/SI-Gen/jportal2-generator-vanguard-sqlalchemy/archive/refs/tags/1.8.zip|stripBaseDir"               
                       
