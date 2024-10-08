# coding: utf-8

"""
    Artifacts API

     Artifacts is an API-based MMO game where you can manage 5 characters to explore, fight, gather resources, craft items and much more.  Website: https://artifactsmmo.com/  Documentation: https://docs.artifactsmmo.com/  OpenAPI Spec: https://api.artifactsmmo.com/openapi.json 

    The version of the OpenAPI document: 1.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class CooldownSchema(BaseModel):
    """
    CooldownSchema
    """ # noqa: E501
    total_seconds: StrictInt = Field(description="The total seconds of the cooldown.")
    remaining_seconds: StrictInt = Field(description="The remaining seconds of the cooldown.")
    started_at: datetime = Field(description="The start of the cooldown.")
    expiration: datetime = Field(description="The expiration of the cooldown.")
    reason: StrictStr = Field(description="The reason of the cooldown.")
    __properties: ClassVar[List[str]] = ["total_seconds", "remaining_seconds", "started_at", "expiration", "reason"]

    @field_validator('reason')
    def reason_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['movement', 'fight', 'crafting', 'gathering', 'buy_ge', 'sell_ge', 'delete_item', 'deposit_bank', 'withdraw_bank', 'equip', 'unequip', 'task', 'recycling']):
            raise ValueError("must be one of enum values ('movement', 'fight', 'crafting', 'gathering', 'buy_ge', 'sell_ge', 'delete_item', 'deposit_bank', 'withdraw_bank', 'equip', 'unequip', 'task', 'recycling')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CooldownSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CooldownSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "total_seconds": obj.get("total_seconds"),
            "remaining_seconds": obj.get("remaining_seconds"),
            "started_at": obj.get("started_at"),
            "expiration": obj.get("expiration"),
            "reason": obj.get("reason")
        })
        return _obj


