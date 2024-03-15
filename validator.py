from __future__ import annotations
from pydantic import ValidationError


def validator_pydantic(data, model):
    try:
        model.model_rebuild()
        validated_data = model(**data)
    except ValidationError as e:
        print(e)
        raise Exception("API response is incorrect")
    else:
        return validated_data
