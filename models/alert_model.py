from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Geocode(BaseModel):
    SAME: List[str]
    UGC: List[str]


class Parameters(BaseModel):
    AWIPSidentifier: List[str]
    WMOidentifier: List[str]
    BLOCKCHANNEL: List[str]


class Properties(BaseModel):
    id: str = Field(..., alias='@id')
    type: str = Field(..., alias='@type')
    id: str
    areaDesc: str
    geocode: Geocode
    affectedZones: List[str]
    references: List
    sent: str
    effective: str
    onset: Any
    expires: str
    ends: Any
    status: str
    messageType: str
    category: str
    severity: str
    certainty: str
    urgency: str
    event: str
    sender: str
    senderName: str
    headline: Any
    description: str
    instruction: str
    response: str
    parameters: Parameters


class AlertModel(BaseModel):
    id: str
    type: str
    geometry: Any
    properties: Properties
