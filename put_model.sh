
set -e


export AUTH_KEY="RYZ2TmkPPfiBcmWI713hWhiE4AQfAdcF"

if [ $# -lt 3 ]; then
    echo "Usage: put_model.sh [rest_api_url] [model file] [log_key]"
    exit 1
fi


REST_API_URL=$1
shift

MODEL_FILE=$1  
shift

LOG_KEY=$1
shift

echo curl -XPOST "${REST_API_URL}/api/log/${LOG_KEY}" \
    -H 'Content-Type:application/json' \
    --data-binary "@${MODEL_FILE}" \
    -H "Authorization:${AUTH_KEY}" | tee get_model.log


curl -XPOST "${REST_API_URL}/api/log/${LOG_KEY}" \
    -H 'Content-Type:application/json' \
    --data-binary "@${MODEL_FILE}" \
    -H "Authorization:${AUTH_KEY}" | tee get_model.log




