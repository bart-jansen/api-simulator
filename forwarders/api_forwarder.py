
import json
import logging
from typing import Optional

from fastapi import Response
from fastapi.responses import FileResponse

from aoai_simulated_api.models import Config, RequestContext

logger = logging.getLogger(__name__)

def initialize(config: Config):
    # enable support for bearer token authentication
    config.auth_bearer_token = "eyBearerTokenHere"
    
    config.generators.append(twin_auth)
    config.generators.append(twin_files)

# Twin Auth endpoint
async def twin_auth(context: RequestContext) -> Optional[Response]:
    is_match, _ = context.is_route_match(request=context.request, path="/api/token", methods=["POST"])
    if not is_match:
        return None

    logger.debug("📁 getting token at oauth endpoint")

    response_data = {
        "access_token": "access_token_here",
        "expires_in": 300,
        "refresh_expires_in": 0,
        "token_type": "Bearer",
        "not-before-policy": 0,
        "scope": "email profile"
    }

    return Response(content=json.dumps(response_data), media_type="application/json", status_code=200)

# Twin Files endpoint
async def twin_files(context: RequestContext) -> Optional[FileResponse]:
    is_match, path_params = context.is_route_match(request=context.request, path="/api/files/{title}", methods=["GET"])
    if not is_match:
        return None

    doc_title = path_params["title"]
    logger.debug("📁 hitting file endpoint for doc: %s", doc_title)
    file_path = "/app/pdfs/sample-asset.pdf"  # Update this path accordingly
    
    return FileResponse(path=file_path, media_type='application/pdf', filename="sample-asset.pdf")
