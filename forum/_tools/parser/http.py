import json
from typing import Any, Dict
from django.http import HttpResponse


def json_resp(content: Dict[Any, Any], status: int):
    return HttpResponse(
        json.dumps(content), status=status, content_type="application/json"
    )
