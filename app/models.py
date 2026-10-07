from __future__ import annotations

import re
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator

# Правила имён bucket S3: 3-63 символа, строчные буквы/цифры/дефис
BUCKET_NAME_RE = re.compile(r"^[a-z0-9][a-z0-9\-]{1,61}[a-z0-9]$")


class BucketCreate(BaseModel):
    name: str = Field(..., examples=["bucket-name-1"], description="Уникальное имя bucket")

    @field_validator("name")
    @classmethod
    def check_name(cls, value: str) -> str:
        if not BUCKET_NAME_RE.match(value):
            raise ValueError(
                "Имя bucket: 3-63 символа, строчные латинские буквы, цифры и дефис; "
                "начинается и заканчивается буквой или цифрой"
            )
        return value


class BucketInfo(BaseModel):
    name: str
    creation_date: Optional[str] = None


class BucketList(BaseModel):
    count: int
    buckets: List[BucketInfo]


class BucketStats(BaseModel):
    name: str
    objects_count: int
    total_size: int


class ObjectInfo(BaseModel):
    key: str
    size: int
    last_modified: Optional[str] = None
    etag: Optional[str] = None


class ObjectList(BaseModel):
    bucket: str
    count: int
    objects: List[ObjectInfo]


class UploadedObject(BaseModel):
    bucket: str
    key: str
    size: int
    content_type: Optional[str] = None


class OperationResult(BaseModel):
    status: str
    resource: str